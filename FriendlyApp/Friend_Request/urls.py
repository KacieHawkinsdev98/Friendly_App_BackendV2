from .views import accept_friend_request, send_friend_request
from django.urls import path 




urlpatterns = [
    path('send_friend_request/<int:userID>/',
    send_friend_request, name='send friend request'),
    
    path('accept_friend_request/<int:requestID>/',
    accept_friend_request, name='accept friend request'),
   
]
