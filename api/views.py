from api.models import Transaction
from api.serializers.transaction_serializer import TransactionSerializer
from rest_framework import generics
from django.shortcuts import render
from django.views import View

class TransactionsScreen(View):
        template_name = 'transactions.html'

def get(self, request):
        return render(request, self.template_name)

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

