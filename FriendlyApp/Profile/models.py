from django.db import models
from django.contrib.auth.models import User



      
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='images/',null=True)
    friends = models.ManyToManyField(User, related_name="+")
    favorite_food = models.CharField(max_length=20, null=True)
    favorite_activity = models.CharField(max_length=30, null=True)
    
    def __str__(self):
     return f'{self.user.username}' 
     

    