from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Status(models.Model):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
