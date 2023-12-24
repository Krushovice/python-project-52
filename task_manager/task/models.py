from django.db import models
from task_manager.user.models import CustomUser
from task_manager.status.models import Status
from task_manager.label.models import Label
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.
class Task(models.Model):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=200,
                            unique=True,
                            )
    description = models.TextField(verbose_name=_('Description'),
                                   max_length=255,
                                   unique=False,
                                   blank=True,
                                   null=True,)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='task_author')
    executor = models.ForeignKey(CustomUser,
                                 verbose_name=_('Executor'),
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 related_name='task_executor')
    labels = models.ManyToManyField(Label,
                                    verbose_name=_('Labels'),
                                    blank=True,
                                    related_name='task_labels')
    status = models.ForeignKey(Status,
                               verbose_name=_('Status'),
                               on_delete=models.PROTECT,
                               related_name='task_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('task_index')

    def __str__(self):
        return f'{self.name}'
