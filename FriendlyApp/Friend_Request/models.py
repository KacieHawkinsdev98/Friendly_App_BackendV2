from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, 
    related_name='from_profile',on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='to_profile', on_delete=models.CASCADE
    )

    
    