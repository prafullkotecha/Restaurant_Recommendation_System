from django.contrib.auth.models import Permission, User
from django.db import models
from django.contrib import admin
from django.forms import ModelForm
# Create your models here.
class Restaurant(models.Model):
    business_id=models.CharField(max_length=250)
    full_address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    review_count =models.IntegerField()
    name =models.CharField(max_length=100)
    longitude=models.FloatField(default=0)
    lattitude=models.FloatField(default=0)
    caters=models.BooleanField(default=True)
    Noise_level=models.CharField(max_length=100)
    Take_Reservations=models.BooleanField()
    Delivery=models.CharField(max_length=100)
    Has_TV=models.BooleanField()
    Outdoor_Seating=models.BooleanField()
    Attire=models.CharField(max_length=100)
    Alcohol=models.CharField(max_length=100)
    Water_service=models.BooleanField()
    Accepts_Credit_card=models.BooleanField()
    good_for_kids=models.BooleanField()
    good_for_groups=models.BooleanField()
    price_range=models.IntegerField()
    Type=models.CharField(max_length=100)

    def __str__(self):
       return self.name + ' - ' + self.city

