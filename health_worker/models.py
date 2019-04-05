from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings

User = settings.AUTH_USER_MODEL

class HealthOfficer(models.Model):
    """
    Description:This is going to represent a health worker.\n
    """
    user = models.OneToOneField(User,primary_key=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = _("Health Officer")
        verbose_name_plural = _("Health Officers")

    def __str__(self):
        return str(self.user.phone_number)

    def get_absolute_url(self):
        pass
        # return reverse("_detail", kwargs={"pk": self.pk})
