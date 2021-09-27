from django.urls import path 
from Profile import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    
]

