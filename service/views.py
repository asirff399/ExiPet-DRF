from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
# Create your views here.
from rest_framework import filters, pagination
class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']