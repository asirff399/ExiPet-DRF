from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Deposite(models.Model):
    user = models.ForeignKey(User, related_name = 'deposite', on_delete = models.CASCADE,null=True) 
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.CharField(max_length=20, default='Deposite')
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['timestamp'] 

class Withdraw(models.Model):
    user = models.ForeignKey(User, related_name = 'withdraw', on_delete = models.CASCADE,null=True) 
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.CharField(max_length=20, default='Withdraw') 
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['timestamp'] 

