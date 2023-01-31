from django.urls import path
from api.views import TransactionList, TransactionDetail, TransactionsScreen

urlpatterns = [
    # path('transactions/', TransactionList.as_view(), name='transaction-list'),
    # path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('transactions/', TransactionsScreen.as_view(), name='transactions_screen'),
]