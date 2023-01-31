from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=16, unique=True)

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debit_transactions')
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credit_transactions')

    def save(self, *args, **kwargs):
        debit_account = self.debit_account
        credit_account = self.credit_account

        debit_account.balance -= self.amount
        credit_account.balance += self.amount

        debit_account.save()
        credit_account.save()

        super().save(*args, **kwargs)
        
class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='ledgers')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='ledgers')
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
