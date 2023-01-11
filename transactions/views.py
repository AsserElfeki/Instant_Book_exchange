import uuid
from itertools import chain

from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import BookReader
from boookzdata.models import Book, BookShelf
from boookzdata.serializers import BookSerializer, NotificationSerializer
from .models import Transaction, TransactionStatus
from .serializers import TransactionSerializer, TransactionRatingSerializer

from rest_framework import generics


class NonExisitingBooksChosen(APIException):
    status_code = 503
    default_detail = 'Books participated in transaction are not existing in database'
    default_code = 'service_unavailable'


class ExternalUserInterfer(APIException):
    status_code = 503
    default_detail = 'You are not allowed to confirm this transaction'
    default_code = 'service_unavailable'


class TransactionsView(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        book_reader = BookReader.objects.get(user=self.request.user)
        user_transactions_as_initiator = Transaction.objects.filter(book_reader_initiator=book_reader)
        user_transactions_as_receiver = Transaction.objects.filter(book_reader_receiver=book_reader)
        return list(chain(user_transactions_as_initiator, user_transactions_as_receiver))


class RateTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        transaction_token = self.kwargs['transaction_token']
        comment = {"comment": self.request.data.get("comment", None)}
        rating = {"rating": self.request.data.get("rating", None)}
        transaction = self.queryset.get(token=transaction_token)
        if transaction:
            current_book_reader = BookReader.objects.get(user=request.user)
            book_reader = {"book_reader": transaction.get_opposite_book_reader(current_book_reader).pk}
            print(book_reader)
            if transaction.transaction_status.name == "Completed":
                transaction = {"transaction": transaction.pk}
                data = {**transaction, **book_reader, **comment, **rating}
                serializer = TransactionRatingSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    rate_instance = serializer.save()

                    content = {"content": "You have received a new rating"}
                    origin = {"origin": "Ratings"}
                    data = {**content, **origin, **book_reader}
                    notification = NotificationSerializer(data=data)
                    if notification.is_valid(raise_exception=True):
                        notification.save()

                    return Response({"success": f"Rate '{rate_instance}' created successfully"})
                return Response({"error": "Transaction is not completed"})
        return Response({"error": "Transaction doesn't exist"})


# View should save these books in serializer and get book_reder_receiver
# token
# book that wants to be received <pk>
# book that will be given <pk>
# user shouldn't initiate transaction with himself
class StartTransactionView(generics.CreateAPIView):
    # queryset = Transaction.objects.none()
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        try:
            initiator_book = Book.objects.get(pk=self.request.data.get("initiator_book", None))
            receiver_book = Book.objects.get(pk=self.request.data.get("receiver_book", None))
        except Exception:
            raise NonExisitingBooksChosen()
        book_reader_initiator = initiator_book.get_book_reader()
        book_reader_receiver = receiver_book.get_book_reader()
        transaction_status, created = TransactionStatus.objects.get_or_create(name="Initiated")
        transaction_saved = serializer.save(token=self.get_token(), book_reader_initiator=book_reader_initiator,
                                            book_reader_receiver=book_reader_receiver,
                                            transaction_status=transaction_status,
                                            initiator_book=initiator_book, receiver_book=receiver_book)

        content = {
            "content": f"{book_reader_initiator.user.username} wants to trade with you. Go to transactions section to respond."}
        origin = {"origin": "Transactions"}
        notification_target = {"book_reader": book_reader_receiver.pk}
        data = {**content, **origin, **notification_target}
        notification = NotificationSerializer(data=data)
        if notification.is_valid(raise_exception=True):
            notification.save()

    def get_token(self):
        return uuid.uuid4()


class DeclineTransactionView(RetrieveUpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def put(self, request, *args, **kwargs):
        transaction_token = self.kwargs['transaction_token']
        transaction = self.queryset.get(token=transaction_token)
        if transaction:
            bad_statuses = ["Accepted", "Completed", "Received by initiating user", "Received by receiving user"]
            if transaction.transaction_status.name not in bad_statuses:
                transaction_status, created = TransactionStatus.objects.get_or_create(name="Declined")
                transaction.transaction_status = transaction_status
                transaction.save()
                serializer = self.get_serializer(transaction, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                book_reader_initiator = transaction.book_reader_initiator
                book_reader_receiver = transaction.book_reader_receiver
                content = {"content": f"Transaction with {book_reader_receiver.user.username} was declined."}
                origin = {"origin": "Transactions"}
                notification_target = {"book_reader": book_reader_initiator.pk}
                data = {**content, **origin, **notification_target}
                notification = NotificationSerializer(data=data)
                if notification.is_valid(raise_exception=True):
                    notification.save()

                return Response(serializer.data)
            return Response({"error": "cannot change status of the transaction"})


class ConfirmTransactionView(RetrieveUpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def put(self, request, *args, **kwargs):
        transaction_token = self.kwargs['transaction_token']
        transaction = self.queryset.get(token=transaction_token)
        if transaction:
            bad_statuses = ["Accepted", "Completed", "Received by initiating user", "Received by receiving user"]
            if transaction.transaction_status.name not in bad_statuses:
                current_book_reader = BookReader.objects.get(user=self.request.user)
                transaction_status, created = TransactionStatus.objects.get_or_create(name="Accepted")
                if transaction.book_reader_receiver == current_book_reader:
                    transaction.transaction_status = transaction_status
                    transaction.save()
                    serializer = self.get_serializer(transaction, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)

                    # search for all transactions with these books and delete them
                    all_transactions_to_decline_1 = self.queryset.filter(initiator_book=transaction.initiator_book)
                    all_transactions_to_decline_2 = self.queryset.filter(initiator_book=transaction.receiver_book)
                    all_transactions_to_decline_3 = self.queryset.filter(receiver_book=transaction.initiator_book)
                    all_transactions_to_decline_4 = self.queryset.filter(receiver_book=transaction.receiver_book)

                    all_to_decline = all_transactions_to_decline_1 | all_transactions_to_decline_2 | all_transactions_to_decline_3 | all_transactions_to_decline_4
                    # exclude current transaction
                    all_to_decline = all_to_decline.exclude(token=transaction_token)

                    # send notifications to both user that transaction was canceled

                    transaction_status_declined, created = TransactionStatus.objects.get_or_create(name="Declined")
                    for trans in all_to_decline:
                        book_reader_initiator = trans.book_reader_initiator
                        book_reader_receiver = trans.book_reader_receiver
                        content = {
                            "content": f"Transaction from {book_reader_initiator.user.username} was canceled because it was involved in another transaction."}
                        origin = {"origin": "Transaction"}
                        notification_target = {"book_reader": book_reader_receiver.pk}
                        data = {**content, **origin, **notification_target}
                        notification = NotificationSerializer(data=data)
                        if notification.is_valid(raise_exception=True):
                            notification.save()

                        content = {
                            "content": f"Transaction to {book_reader_receiver.user.username} was canceled because it was involved in another transaction."}
                        origin = {"origin": "Transaction"}
                        notification_target = {"book_reader": book_reader_initiator.pk}
                        data = {**content, **origin, **notification_target}
                        notification = NotificationSerializer(data=data)
                        if notification.is_valid(raise_exception=True):
                            notification.save()

                        trans.delete()

                    book_reader_initiator = transaction.book_reader_initiator
                    book_reader_receiver = transaction.book_reader_receiver
                    content = {"content": f"Transaction with {book_reader_receiver.user.username} was accepted."}
                    origin = {"origin": "Transaction"}
                    notification_target = {"book_reader": book_reader_initiator.pk}
                    data = {**content, **origin, **notification_target}
                    notification = NotificationSerializer(data=data)
                    if notification.is_valid(raise_exception=True):
                        notification.save()
                return Response("Wait until the transaction is accepted by receiver")
            return Response({"error": "cannot change status of the transaction"})


class ConfirmReceiveTransactionView(RetrieveUpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def put(self, request, *args, **kwargs):
        transaction_token = self.kwargs['transaction_token']
        transaction = self.queryset.get(token=transaction_token)
        if transaction:
            if transaction.transaction_status.name != "Declined" \
                    and transaction.transaction_status.name != "Completed" \
                    and transaction.transaction_status.name == "Accepted" \
                    or transaction.transaction_status.name == "Received by initiating user" \
                    or transaction.transaction_status.name == "Received by receiving user":

                current_book_reader = BookReader.objects.get(user=self.request.user)
                transaction_status = self.get_transaction_status_based_on_current(transaction, current_book_reader)
                transaction.transaction_status = transaction_status
                transaction.save()
                serializer = self.get_serializer(transaction, data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                if transaction_status.name == "Completed":
                    receiver_book, initiator_book = transaction.receiver_book, transaction.initiator_book
                    self.put_books_into_history_shelf(request, receiver_book, initiator_book)
                return Response(serializer.data)
            return Response({"error": "cannot change status of the transaction"})
        return Response("Wait until the transaction is accepted by receiver")

    def put_books_into_history_shelf(self, request, receiver_book, initiator_book):
        history_shelf, created = BookShelf.objects.get_or_create(shelf_name="history")
        receiver_book.book_shelf = history_shelf
        initiator_book.book_shelf = history_shelf
        receiver_book.save()
        initiator_book.save()
        receiver_serializer = BookSerializer(receiver_book, data=request.data)
        initiator_serializer = BookSerializer(initiator_book, data=request.data)
        receiver_serializer.is_valid(raise_exception=True)
        self.perform_update(receiver_serializer)
        initiator_serializer.is_valid(raise_exception=True)
        self.perform_update(initiator_serializer)

    def get_transaction_status_based_on_current(self, transaction, current_book_reader):
        if current_book_reader == transaction.book_reader_receiver:
            if transaction.transaction_status.name == "Received by initiating user":
                transaction_status, created = TransactionStatus.objects.get_or_create(name=f"Completed")
                book_reader = transaction.book_reader_initiator
                content = {
                    "content": f"{current_book_reader.user.username} received your book and transaction was completed."}
            else:
                transaction_status, created = TransactionStatus.objects.get_or_create(
                    name=f"Received by receiving user")
                book_reader = transaction.book_reader_initiator
                content = {"content": f"{current_book_reader.user.username} received your book."}
        elif current_book_reader == transaction.book_reader_initiator:
            if transaction.transaction_status.name == "Received by receiving user":
                transaction_status, created = TransactionStatus.objects.get_or_create(name=f"Completed")
                book_reader = transaction.book_reader_receiver
                content = {
                    "content": f"{current_book_reader.user.username} received your book and transaction was completed."}
            else:
                transaction_status, created = TransactionStatus.objects.get_or_create(
                    name=f"Received by initiating user")

                book_reader = transaction.book_reader_receiver
                content = {"content": f"{current_book_reader.user.username} received your book."}
        else:
            raise ExternalUserInterfer()

        origin = {"origin": "Transaction"}
        notification_target = {"book_reader": book_reader.pk}
        data = {**content, **origin, **notification_target}
        notification = NotificationSerializer(data=data)
        if notification.is_valid(raise_exception=True):
            notification.save()

        return transaction_status
