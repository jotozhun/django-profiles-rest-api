from rest_framework import serializers

from balance_api import models

class BankAccountSerializer(serializers.ModelSerializer):
    """Serializers a bank account object"""
    class Meta:
        model = models.BankAccount
        fields = ('id', 'account_type', 'description', 'balance')
    


class MoneyTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyTransactions
        fields = ('id', 'amount', 'balance', 'description')