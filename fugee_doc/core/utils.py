'''utility methods for the project. '''
import random
import string
import datetime
from django.utils import timezone
from django.utils.text import slugify


ALLOWED_INT = '123456789'
ALLOWED_CHARS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
DONT_USE = ['create']



def custom_string_generator(size=11,chars=ALLOWED_INT+ALLOWED_CHARS):
    return ''.join(random.choice(chars) for _ in range(size))
#unique branch id



def unique_refugee_id_generator(instance,size=4):
    """
    Description:Generate a unique refugee id for every refugee created.\n
    """
    new_refugee_id = custom_string_generator(size=size)
    #Get the class from the instance
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(refugee_id=new_refugee_id).exists()
    if qs_exists:
        return custom_string_generator(size=size)
    
    return new_refugee_id






def unique_entry_id_generator(instance,size=7):
    """
    Description:Generate a unique entry id for every  created.\n
    """
    new_refugee_id = custom_string_generator(size=size)
    #Get the class from the instance
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(entry_id=new_refugee_id).exists()
    if qs_exists:
        return custom_string_generator(size=size)
    
    return new_refugee_id