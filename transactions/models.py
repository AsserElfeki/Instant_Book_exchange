from django.db import models
import uuid

class Transaction(models.Model):
	token = models.CharField(max_length=128)
	book_reader_initiator = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE, related_name='transaction_initiator', related_query_name='transaction_initiator')
	book_reader_receiver = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE, related_name='transaction_receiver', related_query_name='transaction_receiver')
	books = models.ForeignKey('boookzdata.Book', on_delete=models.CASCADE, related_name='transaction_book', related_query_name='transaction_book')

	def __str__(self):
		return self.token