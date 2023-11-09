from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)  # название задачи
    body = models.TextField()  # тело задачи
    timestamp = models.DateTimeField(auto_now_add=True)
