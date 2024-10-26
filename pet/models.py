from django.db import models
from .constants import GENDER_TYPE_CHOICES,ADOPTION_TYPE_CHOICES
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField
# Create your models here.

class PetType(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class Pet(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    pet_type = models.ForeignKey(PetType,on_delete=models.CASCADE) 
    description = models.TextField()
    # image = CloudinaryField('image')
    image = models.CharField(max_length=200) 
    adoption_status = models.CharField(max_length=10, choices=ADOPTION_TYPE_CHOICES,default='Available')    
    gender = models.CharField(max_length=10, choices=GENDER_TYPE_CHOICES)
    age = models.DecimalField(null=True,decimal_places=2,max_digits=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

class Adoption(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    adopted_on = models.DateTimeField(auto_now_add=True)
    pet_price = models.DecimalField(max_digits=10, decimal_places=2)
    balance_after_adoption = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pet.name} Adoption By {self.customer.username}"


    
