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
    CreatePatientSymptomSerializer,
    EntryCreateSerializer,


    CreatePatientSymptomSerializer,
    LocationAddSerializer
)

from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from health_worker.models import HealthOfficer


from accounts.models import User


class RefugeeCreateAPIView(APIView):
    '''
    Description:Create a refugee

    '''
    # permission_classes = (IsAuthenticated,)
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









class EntryCreateAPIView(APIView):
    '''
    Description:Create the entry\n
    Type of request:POST\n
    Request data type:JSON\n
    POST request body: \n
        {
        "longitude":"1233",
        "latitude":"1233",
        "common":"commoncommoncommon",
        "description":"wowow",
        "village":"nairobi",
        "neighborhood":"neighborhoodneighborhoodneighborhood",
        "compound":"compound",
        "refugee":1
        }
    
    '''
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args, **kwargs):
        current_user = request.user.phone_number

        #get this user
        the_user = User.objects.get(phone_number = current_user)

        

        common = request.data['common']
        description = request.data['description']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        village = request.data['village']
        neighborhood = request.data['neighborhood']
        compound = request.data['compound']
        refugee = request.data['refugee']


        #first create the symptoms table

        data = {
            "common":common,
            "description":description
        }

        symptom_serializer = CreatePatientSymptomSerializer(data=data)
        if symptom_serializer.is_valid():
            new_sym = symptom_serializer.save()

            #go ahead and create the location

            loc_data = {
                "latitude":latitude,
                'longitude':longitude,
                'village':village,
                'neighborhood':neighborhood,
                'compound':compound
            }

            location_serializer = LocationAddSerializer(data=loc_data)
            if location_serializer.is_valid():
                new_user_location = location_serializer.save()


                #create the entry here now
                ent_data = {
                    "creator":the_user.id,
                    'refugee':refugee,
                    "symptoms":new_sym.id,
                    "location":new_user_location.id
                }

                entry_serializer = EntryCreateSerializer(data=ent_data)

                if entry_serializer.is_valid():
                    new_entry = entry_serializer.save()


                    success_response = {
                        "success":"Posted"
                    }
                    return Response(success_response,status=status.HTTP_201_CREATED)
                
                return Response(entry_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            return Response(location_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        return Response(symptom_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    