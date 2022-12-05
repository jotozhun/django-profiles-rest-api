from balance_api import serializers, models
from balance_api.permissions import UpdateOwnBankAccount
from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BankAccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BankAccountSerializer
    queryset = models.BankAccount.objects.all()
    permission_classes = (UpdateOwnBankAccount, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the bank account to the logged in user"""
        print(self.request.user)
        # serializer.save(user_profile=self.request.user)

    # def perform_create(self, serializer):
    #     """Sets the bank account to the logged in user"""
    #     serializer.save(user_profile=self.request.user)