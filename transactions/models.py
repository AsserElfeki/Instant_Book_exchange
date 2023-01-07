import datetime
import uuid

from django.db import models
from django.utils import timezone


class TransactionRating(models.Model):
    transaction = models.ForeignKey("transactions.Transaction", on_delete=models.CASCADE, null=True)
    book_reader = models.ForeignKey("authentication.BookReader", on_delete=models.CASCADE,null=True)
    comment = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"token-{self.transaction.token}: {self.rating}"


class TransactionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Books are removed from shelves
class Transaction(models.Model):
    token = models.CharField(max_length=128)
    book_reader_initiator = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE,
                                              related_name='transaction_initiator',
                                              related_query_name='transaction_initiator')
    book_reader_receiver = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE,
                                             related_name='transaction_receiver',
                                             related_query_name='transaction_receiver')
    initiator_book = models.ForeignKey('boookzdata.Book', on_delete=models.CASCADE, related_name='initiator_book',
                                       related_query_name='initiator_book', default="", null=True)
    receiver_book = models.ForeignKey('boookzdata.Book', on_delete=models.CASCADE, related_name='receiver_book',
                                      related_query_name='receiver_book', default="", null=True)
    transaction_status = models.ForeignKey(TransactionStatus, on_delete=models.SET_NULL,
                                           related_name='transaction_status', related_query_name='transaction_status',
                                           default="", null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"status-{self.transaction_status} {str(self.token)} "

    def get_opposite_book_reader(self, current_book_reader):
        if current_book_reader == self.book_reader_initiator:
            return self.book_reader_receiver
        else:
            return self.book_reader_initiator
