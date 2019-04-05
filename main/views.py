from django.shortcuts import render

# Create your views here.
from django.views  import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from refugee.models import Refugee


from accounts.models import User


# @method_decorator([login_required,],name='dispatch')
class HealthWorkerDashboardView(View):
    """
    Description:Render the health worker  dashboard.\n
    """
    template_name  = 'owner/dashboard/index.html'
    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,self.template_name,context)








# @method_decorator([login_required,],name='dispatch')
class AllRefugeesView(View):
    '''
    Description:This is going to list all the refugees for the chv.\n
    '''
    template_name = 'owner/dashboard/all_refugees.html'
    def get(self,request,*args,**kwargs):
        all_refugees = Refugee.objects.all()
        context = {
            "all_refugees":all_refugees
        }
        return render(request,self.template_name,context)






# @method_decorator([login_required,],name='dispatch')
class AllHealthWorkersView(View):
    '''
    Description:This is going to list all the health workers for the chv.\n
    '''
    template_name = 'owner/dashboard/all_workers.html'
    def get(self,request,*args,**kwargs):
        all_officers = User.objects.filter(health_worker=True)
        context = {
            "all_officers":all_officers
        }
        return render(request,self.template_name,context)
        






