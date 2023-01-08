from django.template import context
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from authentication.models import BookReader
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


class TransactionRatingSerializerView(FlexFieldsModelSerializer):
    book_reader = serializers.SerializerMethodField()
    transaction = serializers.SerializerMethodField()
    modified = serializers.SerializerMethodField()

    class Meta:
        model = TransactionRating
        fields = ['transaction', "book_reader", "rating", "comment", 'modified']
        
    def get_modified(self, obj):
        return obj.modified.date()

    def get_transaction(self, obj):
        transaction = TransactionSerializer(obj.transaction, context=self.context).data
        return transaction['token'] if transaction is not None else transaction

    def get_book_reader(self, obj):
        
        book_reader_who_gave_the_rating = obj.transaction.get_opposite_book_reader(obj.book_reader)
        serialized = BookReaderSerializer(book_reader_who_gave_the_rating, context=self.context).data

        return serialized 
