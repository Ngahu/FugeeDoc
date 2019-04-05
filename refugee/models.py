from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from fugee_doc.core.utils import (
    unique_refugee_id_generator,
    unique_entry_id_generator
    )

from accounts.models import User

class Refugee(models.Model):
    '''
    Description:Represent a refugee user.\n #TODO ADD A CREATOR FIELD HERE
    '''
    phone_number = models.CharField(db_index=True,max_length=100,verbose_name='phone number')
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
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = ("Patient Symptom")
        verbose_name_plural = ("Patient Symptoms")

    def __str__(self):
        return self.common

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})









class Location(models.Model):
    '''
    Description:Represent a patients location.\n
    '''
    latitude =  models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    village  = models.CharField(max_length=200)
    neighborhood =  models.CharField(max_length=200)
    compound = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self):
        return self.latitude

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})






class Entry(models.Model):
    '''
    Description:This is going to represent an entry.An entry is a representation of
    interaction in between a CHw and a patient
    '''
    creator =  models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)
    entry_id = models.CharField(max_length=20,blank=True,unique=True)
    refugee = models.ForeignKey(Refugee, on_delete=models.PROTECT)
    symptoms = models.ForeignKey(PatientSymptom, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    

    class Meta:
        verbose_name = ("Entry")
        verbose_name_plural = ("Patients Entries")

    def __str__(self):
        return self.entry_id

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})




def entry_id_pre_save_receiver(sender,instance,*args,**kwargs):
    """
    Description:Create a entry id for every saved refugee.\n
    """
    if not instance.entry_id:
        instance.entry_id = unique_entry_id_generator(instance)


pre_save.connect(entry_id_pre_save_receiver,sender=Entry)

