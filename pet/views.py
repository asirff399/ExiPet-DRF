from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Pet,PetType,Adoption
from customer.models import Customer
from .serializers import PetSerializer,PetTypeSerializer,AdoptionSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.utils import timezone
from django_filters import rest_framework as django_filters
from rest_framework import filters, pagination

from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
# class PetPagination(pagination.PageNumberPagination):
#     page_size = 6 # items per page
#     page_size_query_param = page_size
#     max_page_size = 100

class PetFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__id', lookup_expr='icontains')
    adoption_status = django_filters.CharFilter(field_name='adoption_status', lookup_expr='iexact')

    class Meta:
        model = Pet
        fields = ['author', 'adoption_status']

class PetViewset(viewsets.ModelViewSet):   
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # filter_backends = [filters.SearchFilter]
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = PetFilter
    search_fields = ['pet_type__name','adoption_status','author__id']

    # pagination_class = PetPagination

class PetTypeViewset(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer

class AdoptionViewset(viewsets.ModelViewSet):
    queryset = Adoption.objects.all()
    filter_backends = [filters.SearchFilter]
    serializer_class = AdoptionSerializer
    search_fields = ['customer__id']

class PetList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get(self,request,format=None):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = PetSerializer(data = request.data)
        serializer.author=request.user
        print(request.user)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetails(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_object(self,pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        pet = self.get_object(pk)

        if request.user != pet.author and not request.user.is_staff:
            return Response({"detail": "You do not have permission to edit this pet."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PetSerializer(pet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        pet = self.get_object(pk)

        if request.user != pet.author and not request.user.is_staff:
            return Response({"detail": "You do not have permission to delete this pet."}, status=status.HTTP_403_FORBIDDEN)
        
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InitiatPaymentAPIView(APIView):
    def post(self,request,pet_id):
        print(f'Received request to adopt pet with ID {pet_id}')
        pet = get_object_or_404(Pet,id=pet_id)
        print(f"Pet found: {pet.name}, ID: {pet.id}")

        customer = get_object_or_404(Customer,user=request.user)

        sslcommerz = SSLCOMMERZ({
            'store_id': settings.SSLCOMMERZ_STORE_ID,
            'store_pass': settings.SSLCOMMERZ_STORE_PASSWORD,
            'issandbox': settings.SSLCOMMERZ_SANDBOX_MODE
        })

        post_body = {
            'total_amount': pet.price,
            'currency': 'BDT',
            'tran_id': f'TRX_{pet.id}_{request.user.id}',  # Unique transaction ID
            'success_url':f'http://127.0.0.1:8000/pet/payment/success/{pet_id}',
            'fail_url': f'http://127.0.0.1:8000/pet/payment/failed/',
            'cancel_url': f'http://127.0.0.1:8000/pet/payment/cancel/',
            'cus_name': request.user.username,
            'cus_email': request.user.email,
            'cus_phone': customer.phone,
            'cus_add1': customer.address,
            'cus_city': customer.address,
            'cus_country': 'Bangladesh',
            'shipping_method': 'NO',
            'product_name': pet.name,
            'product_category': pet.pet_type.name,
            'product_profile': 'general'
        }

        response = sslcommerz.createSession(post_body)
        if response['status'] == 'SUCCESS':
            return Response({'payment_url': response['GatewayPageURL']}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Payment initiation failed, please try again later.'}, status=status.HTTP_400_BAD_REQUEST)

class PaymentSuccessAPIView(APIView):
    def post(self,request,pet_id):
        print(f'Received request to adopt pet with ID {pet_id}')
        pet = get_object_or_404(Pet,id=pet_id)
        print(f"Pet found: {pet.name}, ID: {pet.id}")
        customer = request.user
        cus_profile = get_object_or_404(Customer,id=request.user.id)

        if cus_profile.balance >= pet.price:
            cus_profile.balance -= pet.price
            cus_profile.save()

            pet.adoption_status = 'Adopted'
            pet.save()

            adoption = Adoption.objects.create(
                customer=customer,
                pet=pet,
                pet_price=pet.price,
                balance_after_adoption=cus_profile.balance,
            )

            serializer=AdoptionSerializer(adoption)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Insufficient balance to adopt this pet'}, status=status.HTTP_400_BAD_REQUEST)

class PaymentFailAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Payment failed. Please try again.'}, status=status.HTTP_200_OK)

class PaymentCancelAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Payment was canceled.'}, status=status.HTTP_200_OK)


# class AdoptPetAPIView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def put(self,request, pet_id):
#         customer = self.request.user
#         print("customer",customer)
#         print("pet_id",pet_id)
#         try:
#             pet = Pet.objects.get(id=pet_id, adoption_status='Available')
#         except Pet.DoesNotExist:
#             print("test")
#             return Response({"error": "Pet not found or already adopted."}, status=status.HTTP_404_NOT_FOUND)

#         pet_price = pet.price

#         if customer.customer.balance < pet_price:
#             return Response({"error": "Insufficient balance to adopt this pet."}, status=status.HTTP_400_BAD_REQUEST)

#         # Deduct the pet price from the customer's balance
#         customer.customer.balance -= pet_price
#         customer.customer.save()

#         # Update the pet's adoption status
#         pet.adoption_status = 'Adopted'
#         pet.save()

#         # Create a new adoption record
#         adoption = Adoption.objects.create(
#             customer=customer,
#             pet=pet,
#             pet_price=pet_price,
#             balance_after_adoption=customer.customer.balance
#         )

#         # Serialize the adoption record and return it in the response
#         serializer = AdoptionSerializer(adoption)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

