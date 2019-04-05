from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from fugee_doc.core.utils import unique_refugee_id_generator



class Refugee(models.Model):
    '''
    Description:Represent a refugee user.\n #TODO ADD A CREATOR FIELD HERE
    '''
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    refugee_id = models.CharField(max_length=100,unique=True,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    

    class Meta:
        verbose_name = ("Refugee")
        verbose_name_plural = ("Refugees")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})





def refugee_id_pre_save_receiver(sender,instance,*args,**kwargs):
    """
    Description:Create a unique id for every saved refugee.\n
    """
    if not instance.refugee_id:
        instance.refugee_id = unique_refugee_id_generator(instance)


pre_save.connect(refugee_id_pre_save_receiver,sender=Refugee)








class PatientSymptom(models.Model):
    '''
    Description:Represent the different symptoms a patient suffers from.\n
    '''
    common = models.TextField(blank=True)
    description = models.TextField(blank=True)

    

    class Meta:
        verbose_name = ()
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})