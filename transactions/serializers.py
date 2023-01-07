import uuid

from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from authentication.serializers import BookReaderSerializer
from .models import Transaction, TransactionStatus, TransactionRating


class TransactionStatusSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ['name', ]


class TransactionSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=False, max_length=64)
    book_reader_initiator = BookReaderSerializer(required=False)
    book_reader_receiver = BookReaderSerializer(required=False)
    transaction_status = serializers.SerializerMethodField()
    created = serializers.DateField(read_only=True)

    class Meta:
        model = Transaction
        fields = (
            'token', 'book_reader_initiator', 'book_reader_receiver', 'initiator_book', 'receiver_book',
            'transaction_status', 'created')

    def get_transaction_status(self, obj):
        image = TransactionStatusSerializer(obj.transaction_status, read_only=True, context=self.context).data['name']
        return image


class TransactionRatingSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = TransactionRating
        fields = ['transaction', "book_reader", "rating", "comment", 'modified']

