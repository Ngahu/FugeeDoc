from django.conf.urls  import url 

from .views import (
    HealthOfficerSendCodeAPIView,
    HealthOfficerConfirmCodeAPIView,
    HealthOfficerRegisterAPIView,
    ATCallBackAPIView
    )


urlpatterns = [

    url('send-code/$', HealthOfficerSendCodeAPIView.as_view(), name='send_code_api_view'),
    url('confirm-code/$', HealthOfficerConfirmCodeAPIView.as_view(), name='confirm_code_api_view'),
    url('register/$', HealthOfficerRegisterAPIView.as_view(), name='register_health_officer'),
    url('callback/$', ATCallBackAPIView.as_view(), name='call_back'),
    

]