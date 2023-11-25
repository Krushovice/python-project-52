from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_update_url(self):
        return reverse('user_update', kwargs={'id': self.id})

    def get_absolute_delete_url(self):
        return reverse('user_delete', kwargs={'id': self.id})

    def __str__(self):
        return self.login
