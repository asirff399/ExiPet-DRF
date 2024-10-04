from django.contrib import admin
from .models import Deposite,Withdraw
# from transactions.models import Transaction
admin.site.register(Deposite)
admin.site.register(Withdraw)