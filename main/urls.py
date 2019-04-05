from django.conf.urls  import url 

from .views import (
    HealthWorkerDashboardView,
    AllRefugeesView,
    AllHealthWorkersView
    )


urlpatterns = [

    url('home/$', HealthWorkerDashboardView.as_view(), name='worker_dashboard_view'),
    url('all-refugees/$', AllRefugeesView.as_view(), name='all_refugees'),
    url('health-workers/$', AllHealthWorkersView.as_view(), name='officers_health'),


]