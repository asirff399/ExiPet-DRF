from rest_framework import serializers
from .models import Pet,PetType,Adoption

class PetSerializer(serializers.ModelSerializer):
    pet_type = serializers.SlugRelatedField(slug_field='name', queryset=PetType.objects.all())
    author = serializers.StringRelatedField(many=False)
    class Meta:
        model = Pet
        fields = ['id','author','name','description','image','adoption_status','gender','pet_type','age','created_on','price',]
        read_only_fields = ['author','id','created_on',]

class AdoptionSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    pet_image = serializers.CharField(source='pet.image', read_only=True)
    customer = serializers.StringRelatedField(many=False)
    class Meta:
        model = Adoption
        fields = '__all__'

class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'