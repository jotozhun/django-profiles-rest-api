from django.contrib import admin
from balance_api import models

# Register your models here.
admin.site.register(models.MoneyTransactions)

@admin.register(models.BankAccount)
class BankAccountAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['account_type']
        else:
            return []