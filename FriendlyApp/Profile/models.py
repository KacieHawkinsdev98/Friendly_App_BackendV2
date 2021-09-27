from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True)
    friends = models.ManyToManyField(User, related_name="+")
    food_preferences = models.CharField(null=True,max_length=50)
    interests = models.CharField(null=True,max_length=50)
    

    def __str__(self):
     return f'{self.user.username}' 
# Create your models here.

