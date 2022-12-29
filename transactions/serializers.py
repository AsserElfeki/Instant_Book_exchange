import uuid

from rest_framework import serializers
from authentication.serializers import BookReaderSerializer
from boookzdata.serializers import BookSerializer
from .models import Transaction


class StartTransaction(serializers.ModelSerializer):
    token = serializers.CharField(required=False,max_length=64)
    book_reader_initiator = BookReaderSerializer(required=False)
    book_reader_receiver = BookReaderSerializer(required=False)
    wanted_book = BookSerializer(required=False)
    giveaway_book = BookSerializer(required=False)

    class Meta:
        model = Transaction
        fields = ('token', 'book_reader_initiator', 'book_reader_receiver', 'wanted_book', 'giveaway_book')

