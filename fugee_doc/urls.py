
from rest_framework.authtoken import views
from django.conf.urls import include,url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^health-worker/', include('health_worker.urls',namespace='health_worker')),
    url(r'^refugee/', include('refugee.urls',namespace='refugee')),


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

