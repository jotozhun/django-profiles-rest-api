from django.db import models
from django.conf import settings


# Create your models here.
class BankAccount(models.Model):
    """Bank account"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    account_type = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    balance = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.account_type


class MoneyTransactions(models.Model):
    """Transactions of balance between Accounts"""
    bank_account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    balance = models.FloatField()
    description = models.CharField(max_length=255)


