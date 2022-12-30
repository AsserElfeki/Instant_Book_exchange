import uuid

from django.db import models

# Initiated
# Accepted
# Received by receiving user
# Received by initiating user
# Completed
class TransactionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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
    transaction_status = models.ForeignKey(TransactionStatus, on_delete=models.SET_NULL,
                                           related_name='transaction_status', related_query_name='transaction_status',
                                           default="", null=True)

    def __str__(self):
        return f"status-{self.transaction_status} {str(self.token)} "
