from django.urls import path, include

from transactions.views import StartTransactionView, ConfirmTransactionView

urlpatterns = [
    path('confirm/<str:transaction_token>', ConfirmTransactionView.as_view(), name='confirm_transaction'),
    path('startTransaction/', StartTransactionView.as_view(), name='start_transaction'),
]
