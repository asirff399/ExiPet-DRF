from django.contrib import messages
from django.template.loader import render_to_string
from datetime import datetime
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from customer.models import Customer
from rest_framework.response import Response
from rest_framework import status
from pet.models import Pet,Adoption
# Create your views here.
import uuid
import base64
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_lib import SSLCOMMERZ 
from django.contrib.auth.models import User

class InitiatePaymentView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, pet_id):
        transaction_id = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').rstrip('=')
        pet = get_object_or_404(Pet, id=pet_id)
        cus_user = Customer.objects.get(user=request.user)
        amount = int(pet.price)

        settings = {'store_id': 'exipe6719a3b69d208', 'store_pass': 'exipe6719a3b69d208@ssl', 'issandbox': True }

        sslcz = SSLCOMMERZ(settings)
        post_body = {
            'total_amount': pet.price,
            'currency': "BDT",
            'tran_id': transaction_id,
            'success_url': f'https://exi-pet-drf.vercel.app/transaction/payment/success/{request.user.id}/{pet_id}/{amount}/{transaction_id}',
            'fail_url': 'https://exi-pet-drf.vercel.app/transaction/payment/fail/',
            'cancel_url': 'https://exi-pet-drf.vercel.app/transaction/payment/cancel/',
            'emi_option': 0,
            'cus_name': request.user.username,
            'cus_email': request.user.email,
            'cus_phone': cus_user.phone,
            'cus_add1': cus_user.address,
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': pet.name,
            'product_category': pet.pet_type,
            'product_profile': "general"
        }

        response = sslcz.createSession(post_body)
        if response and 'GatewayPageURL' in response:
            return JsonResponse({'gateway_url': response['GatewayPageURL']})
        else:
            return JsonResponse({'error': 'Failed to initiate payment'}, status=400)
    
@csrf_exempt
def payment_success(request,user_id,pet_id,amount,tran_id):

    if not amount or not pet_id or not tran_id or not user_id:
        return HttpResponse("Invalid payment details", status=400)
    
    try:
        pet = get_object_or_404(Pet,id=pet_id)

        if pet.adoption_status != "Available":
            return HttpResponse("This pet is already adopted or unavailable", status=400)
        
        pet.adoption_status = "Adopted"
        pet.save()

        user = get_object_or_404(User,id=user_id)

        adoption = Adoption.objects.create(
            customer = user,
            pet = pet,
            pet_price = amount,
            transaction_id = tran_id
        )
        adoption.save()

    except Exception as e:
        return HttpResponse(f"Error updating post: {str(e)}", status=500)
    
    return render(request, "payment_success.html", {"amount": amount, "pet": pet , "tran_id": tran_id, "user":user})


@csrf_exempt
def payment_fail(request):
    return render(request, "payment_fail.html",{"message": "Payment failed !!"},status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def payment_cancel(request):
    return render(request, "payment_cancel.html",{"message": "Payment canceled !!"},status=status.HTTP_200_OK)