from rest_framework import serializers
from .models import Deposite,Withdraw
from customer.models import Customer 

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposite
        fields = ['user','amount']
        read_only_fields = ['user',]

    def validate_amount(self, value):
        min_deposit_amount = 100
        if value < min_deposit_amount:
            raise serializers.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return value

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ['user','amount']
        read_only_fields = ['user',]

    def validate_amount(self, value):
        user = self.context['request'].user
        customer, created = Customer.objects.get_or_create(user=user)

        min_withdraw_amount = 100
        max_withdraw_amount = 20000
        balance = customer.balance

        if value < min_withdraw_amount:
            raise serializers.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )
        elif value > max_withdraw_amount:
            raise serializers.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )
        elif value > balance:
            raise serializers.ValidationError(
                f'You have {balance} $ in your account. '
                'You cannot withdraw more than your account balance'
            )
        
        return value
