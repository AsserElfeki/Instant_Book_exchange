from django.urls import path, include

from transactions.views import StartTransactionView

urlpatterns = [
    path('startTransaction/', StartTransactionView.as_view(), name='list_book_reader'),
]
