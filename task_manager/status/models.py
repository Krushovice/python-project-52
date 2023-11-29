from django.db import models
from task_manager.task.models import Task


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=200)  # название задачи
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Task, related_name='statuses')

    def __str__(self):
        return self.name
