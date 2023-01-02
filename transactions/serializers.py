import uuid

from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from authentication.serializers import BookReaderSerializer
from boookzdata.serializers import BookSerializer
from .models import Transaction, TransactionStatus


class TransactionStatusSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ['name', ]


class TransactionSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=False, max_length=64)
    book_reader_initiator = BookReaderSerializer(required=False)
    book_reader_receiver = BookReaderSerializer(required=False)
    initiator_book = BookSerializer(required=False)
    receiver_book = BookSerializer(required=False)
    transaction_status = TransactionStatusSerializer(required=False)

    class Meta:
        model = Transaction
        fields = (
        'token', 'book_reader_initiator', 'book_reader_receiver', 'initiator_book', 'receiver_book', 'transaction_status')
