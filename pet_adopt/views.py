from django.contrib.auth.models import User 

from rest_framework import viewsets
from . import serializers
from pet.models import Pet

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class AllPetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = serializers.AllPetSerializer
