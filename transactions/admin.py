from django.contrib import admin

from transactions.models import Transaction,TransactionStatus, TransactionRating

admin.site.register(Transaction)
admin.site.register(TransactionStatus)
admin.site.register(TransactionRating)


# Register your models here.
