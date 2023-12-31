from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name=_('First name'),
                                  max_length=255)
    last_name = models.CharField(verbose_name=_('Last name'),
                                 max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
