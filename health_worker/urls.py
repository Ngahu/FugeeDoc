from django.conf.urls  import url 

from .views import (
    HealthOfficerSendCodeAPIView,
    HealthOfficerConfirmCodeAPIView,
    ATCallBackAPIView
    )


urlpatterns = [

    url('send-code/$', HealthOfficerSendCodeAPIView.as_view(), name='send_code_api_view'),
    url('confirm-code/$', HealthOfficerConfirmCodeAPIView.as_view(), name='confirm_code_api_view'),
    url('callback/$', ATCallBackAPIView.as_view(), name='call_back'),
    

]