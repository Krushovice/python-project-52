from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Task
from .forms import TaskCreationForm, TaskUpdateForm
from django.utils.translation import gettext as _
from django.contrib import messages


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()[:15]
        return render(request, 'tasks/index.html', context={
            'tasks': tasks
        })


class TaskShowView(View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)

        return render(request, 'tasks/show.html', context={
            'task': task,
            'task_id': task_id,
        })


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'tasks/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        pass
