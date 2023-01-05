from django.urls import path, include

from transactions.views import StartTransactionView, ConfirmTransactionView, ConfirmReceiveTransactionView, \
    TransactionsView, DeclineTransactionView, RateTransactionView

urlpatterns = [
    path('myTransactions/', TransactionsView.as_view(), name='get_transactions'),
    path('confirm/<str:transaction_token>', ConfirmTransactionView.as_view(), name='confirm_transaction'),
    path('decline/<str:transaction_token>', DeclineTransactionView.as_view(), name='decline_transaction'),
    path('confirmReceive/<str:transaction_token>', ConfirmReceiveTransactionView.as_view(), name='confirm_receive_transaction'),
    path('startTransaction/', StartTransactionView.as_view(), name='start_transaction'),
    path('rate/<str:transaction_token>', RateTransactionView.as_view(), name='rate_transaction'),
]
