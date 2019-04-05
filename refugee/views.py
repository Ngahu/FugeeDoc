import random
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import Refugee

from .serializers import(
    RefugeeRegisterSerializer,
    RefugeeListSerializer,
    CreatePatientSymptomSerializer
)

from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from health_worker.models import HealthOfficer




class RefugeeCreateAPIView(APIView):
    '''
    Description:Create a refugee
    '''
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args, **kwargs):
        first_name = request.data["first_name"]
        last_name =  request.data["last_name"]


        data = {
            "first_name":first_name,
            "last_name":last_name
        }

        #create the refugee

        refugee_create_serializer = RefugeeRegisterSerializer(data=data)

        if refugee_create_serializer.is_valid():
            new_refugee = refugee_create_serializer.save()


            success_response = {
                "first_name":first_name,
                "last_name":last_name
            }
            return Response(success_response,status=status.HTTP_201_CREATED)
        
        return Response(refugee_create_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        






class RefugeeListAPIView(APIView):
    '''
    Description:List down all refugees in the db.\n
    '''
    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        current_user = request.user

        if not HealthOfficer.objects.filter(user=current_user).exists():
            not_officer_error = {
                "error":"Sorry you must be a health officer to access."
            }
            return Response(not_officer_error,status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            refugees_list = Refugee.objects.all()
        
        except Refugee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        refugees_serializer = RefugeeListSerializer(refugees_list,many=True)
        return Response(refugees_serializer.data,status=status.HTTP_200_OK)





