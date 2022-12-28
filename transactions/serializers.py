import uuid

from rest_framework import serializers
from authentication.serializers import BookReaderSerializer
from .models import Transaction


class StartTransaction(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    book_reader_initiator = BookReaderSerializer()
    book_reader_receiver = BookReaderSerializer()

    class Meta:
        model = Transaction
        fields = ('token', 'book_reader_initiator', 'book_reader_receiver')

    def get_token(self, obj):
        return uuid.uuid4()
