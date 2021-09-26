from rest_framework import serializers
from .models import Friend_Request



class Friend_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend_Request
        fields = ['from_profile', 'to_profile']