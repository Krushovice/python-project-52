from django.db import models
from task_manager.user.models import CustomUser
from task_manager.status.models import Status
from task_manager.label.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            )  # название задачи
    description = models.TextField(max_length=255,
                                   unique=False,
                                   blank=True,
                                   null=True,)  # тело задачи
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='author')
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 related_name='executor')
    labels = models.ManyToManyField(Label, blank=True, related_name='labels')
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               related_name='status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
