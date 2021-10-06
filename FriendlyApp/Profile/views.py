from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from .models import Profile
from rest_framework.response import Response 
from rest_framework import status


def index(request):
    return render(request, 'Profile/index.html')


class ProfileList(APIView):

    

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    
    def get_object(self, pk):
        try:
          return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
           raise Http404     

    def get(self, request, pk):
        profiles = self.get_object(pk)
        serializer = ProfileSerializer(profiles)
        return Response(serializer.data)

    def update(self, request, pk):
        profiles = self.get_object(pk)
        serializer = ProfileSerializer(profiles, data=request.data)
        if serializer.is_valid():
            serializer.update(profiles, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
   
   
    def delete(self, request, pk):
        profiles = self.get_object(pk)
        serializer = ProfileSerializer(profiles)
        profiles.delete()
        return Response(serializer.data) 


   





# Create your views here.
