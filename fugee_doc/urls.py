
from rest_framework.authtoken import views
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^health-worker/', include('health_worker.urls',namespace='health_worker')),
    url(r'^refugee/', include('refugee.urls',namespace='refugee')),
]


