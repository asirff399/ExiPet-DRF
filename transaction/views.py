from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Deposite,Withdraw
from customer.models import Customer
from .serializers import DepositSerializer,WithdrawSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DeposiMoneyAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def put(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = DepositSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            amount = serializer._validated_data['amount']
            customer = user.customer
            customer.balance += amount
            customer.save(update_fields=['balance'])

            serializer.save(user=user,balance_after_transaction = customer.balance)

            try:
                email_subject = "Deposit Message"
                email_body = render_to_string('deposit_email.html',{'user':user,'amount':amount})
                email = EmailMultiAlternatives(email_subject,'',to=[user.email])
                email.attach_alternative(email_body,"text/html")
                email.send()
            except Exception as e:
                print(f"Failed to send email: {e}")

            return Response({"success":"Amount deposited successfully!"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WithdrawMoneyAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def put(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = WithdrawSerializer(data=request.data, context={'request': request})
        user = request.user

        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            customer = user.customer

            if customer.balance < amount:
                return Response({"error": "Insufficient Balance"}, status=status.HTTP_400_BAD_REQUEST)
            
            customer.balance -= amount
            customer.save(update_fields = ['balance'])

            serializer.save(user=user, balance_after_transaction = customer.balance)

            try:
                email_subject = "Withdrawal Message"
                email_body = render_to_string('withdrawal_email.html',{'user':user,'amount': amount})
                email = EmailMultiAlternatives(email_subject,'', to=[user.email])
                email.attach_alternative(email_body,"text/html")
                email.send()
            except Exception as e:
                print(f"Failed to send email: {e}")

            return Response({"success": "Amount withdrawn successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

