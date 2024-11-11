from django.db import models
from django.contrib.auth.models import User
from .constants import USER_TYPE_CHOICES,STAR_CHOICES
from pet.models import Pet
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.CharField(max_length=200,default='https://i.ibb.co.com/80NSbds/dummy-profile.png') 
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=200)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES,default='User')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Review(models.Model):
    reviewer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=20,choices=STAR_CHOICES)

    def __str__(self):
        return f"Reviewer: {self.reviewer.user.first_name}; Pet: {self.pet.name}"

    

