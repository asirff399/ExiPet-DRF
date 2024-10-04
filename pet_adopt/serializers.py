from rest_framework import serializers
from django.contrib.auth.models import User 
from pet.models import Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name', 'last_name', 'email', 'is_superuser']

class AllPetSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Pet
        fields = fields = '__all__'