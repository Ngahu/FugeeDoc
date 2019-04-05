import random
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import User

from accounts.serializers import UserSerializer

from .models import HealthOfficer


import africastalking

username = 'sandbox'
api_key = '225578ada51f5897b086a45ea32e65484e55c5c437d6e5b155ae7eeef634bfcf'

# username = 'e_limu'
# api_key = '2647af47e57eaa6130472ff3fdd0b31a8196a76ae2a181aba7daf00a5ca9c398'
africastalking.initialize(username,api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS




class HealthOfficerSendCodeAPIView(APIView):
    """
    Description:Authenticate a health officer\n
    Type of request:POST\n
    Request data type:JSON\n
    POST request body: \n
        {
            "phone_number":"+254725743069"
        }\n
    """
    def post(self,request,*args, **kwargs):
        the_phone_number = request.data['phone_number']
        the_recipient = []

        if " " in the_phone_number:
            error = {
                "error":"Sorry phone number should not have spaces"
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        
        user = User.objects.filter(Q(phone_number=the_phone_number)).distinct()

        #check to make sure that the user is a company owner
        qs = HealthOfficer.objects.filter(user__phone_number=the_phone_number)

        if qs.exists():
            pass
        
        else:
            error = {
                "error":"The phone number or password you entered is incorrect. Please try again.Does not exist as a health officer"
            }
            return Response(error,status=status.HTTP_401_UNAUTHORIZED)
        
        if user.exists and user.count() ==1:
            user_object = user.first()
        
        else:
            error = {
                "error":"The phone number or password you entered is incorrect. Please try again."
            }
            return Response(error,status=status.HTTP_403_FORBIDDEN)
        
        if user_object:

            #Generate the code here and set it as the password here and send it to the user's phone number 
            '''
            First Generate  a new code for the user
            Then save it as the users password
            Then send the code to the users phone number
            '''

            #get the health officer 
            try:
                the_health_officer = User.objects.get(phone_number=the_phone_number)
            
            except User.DoesNotExist:
                error = {
                    "error":"Sorry,the phone number or password you entered is incorrect. Please try again. "
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)


            int_numbers = random.sample(range(10), 4)

            the_code = ''.join(map(str, int_numbers))

            # print(the_code)

            # print(the_health_officer)
            # print("the officer",the_health_officer.phone_number)

            # phone_no = the_health_officer.phone_number
            # print("phone no",phone_no)



            data = {
                "phone_number":the_health_officer.phone_number,
                "first_name": the_health_officer.first_name,
                "last_name": the_health_officer.last_name,
                
            }

            serializer_class = UserSerializer(the_health_officer,data=data, partial=True)

            if serializer_class.is_valid():
                user = serializer_class.save()             
                user.set_password(the_code)
                user.save()


                #send the code to the user here
                the_recipient.append(str(the_health_officer.phone_number))

                message = "FugeeDoc, your code is {}".format(the_code)

                res = sms.send(message=message,recipients=the_recipient)

                print(res)
                



                success_response = {
                    "success":"Code sent to {}".format(the_health_officer.phone_number)
                }
                return Response(success_response,status=status.HTTP_202_ACCEPTED)

            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)









class HealthOfficerConfirmCodeAPIView(APIView):
    """
    Description:Authenticate a health officer\n
    Type of request:POST\n
    Request data type:JSON\n
    POST request body: \n
        {
            "email":"+254725743069",
            "code":"1234"
        }\n
    Response success status:HTTP_201_created \n
    Response data type:JSON\n
    Sample success Response: \n
                                {
                                    "user": 1,
                                    "phone_number": "+254725743069",
                                    "key": "efdf1021940672734726abbe04e434199214c759"
                                }\n    
    Response failure: \n
    {
        "error": "The phone number or password you entered is incorrect. Please try again."
    }\n
    """
    def post(self,request,*args, **kwargs):
        the_phone_number = request.data['phone_number']
        password = request.data['code']

        if " " in the_phone_number:
            error = {
                "error":"Sorry phone number should not have spaces"
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        
        user = User.objects.filter(Q(phone_number=the_phone_number)).distinct()

        #check to make sure that the user is a company owner
        qs = HealthOfficer.objects.filter(user__phone_number=the_phone_number)

        if qs.exists():
            pass
        
        else:
            error = {
                "error":"The code you entered is incorrect. Please try again."
            }
            return Response(error,status=status.HTTP_401_UNAUTHORIZED)
        
        if user.exists and user.count() ==1:
            user_object = user.first()
        
        else:
            error = {
                "error":"The code you entered is incorrect. Please try again."
            }
            return Response(error,status=status.HTTP_403_FORBIDDEN)
        
        if user_object:
            #check the users password
            if not user_object.check_password(password):
                error = {
                    "error":"The code you entered is incorrect. Please try again."
                }
                return Response(error,status=status.HTTP_403_FORBIDDEN)

            try:
                token = Token.objects.get(user_id=user_object.id)

                success_login_response = {
                    "key":token.key,
                    "phone_number":user_object.phone_number,
                    "first_name":user_object.first_name,
                    "last_name":user_object.last_name
                }
                return Response(success_login_response,status=status.HTTP_200_OK)
            
            except Token.DoesNotExist:
                error = {
                    "error":"Sorry This  user is not active please contact us!"
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)

















class ATCallBackAPIView(APIView):
    '''
    Description:AT Callback\n
    Type of request:POST\n
    Request data type:JSON\n
    POST request body: \n
        {
            "response":"user response is posted here."
        }\n
    '''
    def post(self,request,*args, **kwargs):
        sessionId = request.data['sessionId']
        serviceCode = request.data['serviceCode']
        phoneNumber = request.data['phoneNumber']
        the_text = request.data['text']

        response = ''


        print("The users data",the_text)

        if the_text == "":
            response  = "CON What would you want to check \n`
            response  = "1. My Account \n"
            response  = "2. My phone number"
        
        else:
            print("Not empty")

        # if not the_text:
        #     print("the text is empty")
        #     response = `CON What would you like to check 1.My Account 2.My phone number`
        # else:
        #     print("not empty")




        
        return Response(response,status=status.HTTP_202_ACCEPTED)
