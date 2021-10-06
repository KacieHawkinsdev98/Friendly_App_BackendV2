from django.db import models
from .models import User

# Create your models here.

class FriendDate(models.Model):
    friendDates=models.OneToOneField(User, on_delete=models.CASCADE)
    suggestedDates=models.CharField(null=True, max_length=200)
    categories=models.CharField(null=True, max_length=200)
    