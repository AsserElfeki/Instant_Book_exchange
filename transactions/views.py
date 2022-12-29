import uuid

from django.http import QueryDict
from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.models import BookReader
from boookzdata.models import Book
from boookzdata.views import NotCorrectUrlProvided
from .models import Transaction
from .serializers import StartTransaction

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
class StartTransactionView(generics.CreateAPIView):
    # queryset = Transaction.objects.none()
    permission_classes = (IsAuthenticated,)
    serializer_class = StartTransaction

    def perform_create(self, serializer):
        try:
            giveaway_book = Book.objects.get(pk=self.request.data.get("giveaway_book", None))
            wanted_book = Book.objects.get(pk=self.request.data.get("wanted_book", None))
        except Exception:
            raise NonExisitingBooksChosen()
        book_reader_initiator = giveaway_book.get_book_reader()
        book_reader_receiver = wanted_book.get_book_reader()
        serializer.save(token=self.get_token(), book_reader_initiator=book_reader_initiator,
                        book_reader_receiver=book_reader_receiver,
                        giveaway_book=giveaway_book, wanted_book=wanted_book)

    def get_token(self):
        return uuid.uuid4()
