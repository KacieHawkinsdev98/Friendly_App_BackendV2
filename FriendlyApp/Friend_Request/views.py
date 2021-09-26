from FriendlyApp.Friend_Request.models import Friend_Request
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse 
from .models import User
from rest_framework import status


@login_required 
def send_friend_request(request, userID):
    from_user = request.user 
    to_user = User.objects.get(id=to_userID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created: 
        return HttpResponse('friend request sent')
    else: 
        return HttpResponse('friend request was already sent')


@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.from_user)
        return HttpResponse ('friend request accecpted')
    else:
        return HttpResponse ('friend request not accecpted')


# Create your views here.
