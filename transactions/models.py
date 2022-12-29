import uuid

from django.db import models


class Transaction(models.Model):
    token = models.CharField(max_length=128)
    book_reader_initiator = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE,
                                              related_name='transaction_initiator',
                                              related_query_name='transaction_initiator')
    book_reader_receiver = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE,
                                             related_name='transaction_receiver',
                                             related_query_name='transaction_receiver')
    wanted_book = models.ForeignKey('boookzdata.Book', on_delete=models.CASCADE, related_name='wanted_book',
                                    related_query_name='wanted_book', default="", null=True)
    giveaway_book = models.ForeignKey('boookzdata.Book', on_delete=models.CASCADE, related_name='giveaway_book',
                                      related_query_name='giveaway_book', default="", null=True)

    def __str__(self):
        return str(self.token)
