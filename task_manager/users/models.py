# from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    pswrd = models.CharField(('password'), max_length=128)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login
