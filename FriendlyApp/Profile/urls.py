from django.urls import path 
from Profile import views


app_name = "Profile"
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileList.as_view()),
    path('<int:pk>/profile/', views.ProfileDetail.as_view()),
    path('<int:pk>/delete/',views.ProfileDetail.as_view()),
    path('<int:pk>/update/',views.ProfileDetail.as_view())
    
]

