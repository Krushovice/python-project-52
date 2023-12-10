from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Task


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


class TaskUpdateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
