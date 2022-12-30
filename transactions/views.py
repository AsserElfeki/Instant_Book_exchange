import uuid

from django.http import QueryDict
from django.shortcuts import render
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from authentication.models import BookReader
from boookzdata.models import Book
from boookzdata.views import NotCorrectUrlProvided
from .models import Transaction, TransactionStatus
from .serializers import TransactionSerializer

from rest_framework import generics, status
from django.shortcuts import get_object_or_404


class NonExisitingBooksChosen(APIException):
    status_code = 503
    default_detail = 'Books participated in transaction are not existing in database'
    default_code = 'service_unavailable'


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
            giveaway_book = Book.objects.get(pk=self.request.data.get("giveaway_book", None))
            wanted_book = Book.objects.get(pk=self.request.data.get("wanted_book", None))
        except Exception:
            raise NonExisitingBooksChosen()
        book_reader_initiator = giveaway_book.get_book_reader()
        book_reader_receiver = wanted_book.get_book_reader()
        transaction_status, created = TransactionStatus.objects.get_or_create(name="Initiated")
        serializer.save(token=self.get_token(), book_reader_initiator=book_reader_initiator,
                        book_reader_receiver=book_reader_receiver, transaction_status=transaction_status,
                        giveaway_book=giveaway_book, wanted_book=wanted_book)

    def get_token(self):
        return uuid.uuid4()


class ConfirmTransactionView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def update(self, request, *args, **kwargs):
        transaction_token = self.kwargs['transaction_token']
        transaction = self.queryset.get(token=transaction_token)
        transaction_status = TransactionStatus.objects.get_or_create(name="Accepted")
        if transaction:
            current_book_reader = BookReader.objects.get(user=self.request.user)
            if transaction.get().book_reader_receiver == current_book_reader:
                transaction.transaction_status = transaction_status
                transaction.save()
        serializer = self.get_serializer(transaction)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
