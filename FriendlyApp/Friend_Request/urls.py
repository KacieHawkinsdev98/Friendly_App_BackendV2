from FriendlyApp.Friend_Request.views import accept_friend_request, send_friend_request
from django.urls import path 
from Friend_Request import views



urlpatterns = [
    path('send_friend_request/<int:userID>/',
    send_friend_request, name='send friend request'),
    
    path('accept_friend_request/<int:requestID>/',
    accept_friend_request, name='accept friend request'),
   
]
