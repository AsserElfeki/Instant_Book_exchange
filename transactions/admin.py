from django.contrib import admin

from transactions.models import Transaction,TransactionStatus

admin.site.register(Transaction)
admin.site.register(TransactionStatus)


# Register your models here.
