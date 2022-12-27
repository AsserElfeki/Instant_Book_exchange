from django.core.serializers import serialize
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
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

