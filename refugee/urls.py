from django.conf.urls  import url 

from .views import (
    RefugeeCreateAPIView,
    RefugeeListAPIView
    )


urlpatterns = [

    url('create/$', RefugeeCreateAPIView.as_view(), name='create_refugee'),
    url('list-refugees/$', RefugeeListAPIView.as_view(), name='list_refugee'),
    

]