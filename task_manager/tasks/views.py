from django.shortcuts import render, get_object_or_404
from django.views import View
from task_manager.tasks.models import Task


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()[:15]
        return render(request, 'tasks/index.html', context={
            'tasks': tasks
        })


class TaskView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['id'])
        return render(request, 'tasks/show.html', context={
            'task': task,
        })
