from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic.edit import CreateView
from .models import Task
from task_manager.user.models import CustomUser
from task_manager.status.models import Status
from task_manager.label.models import Label
from .forms import TaskForm
from .filters import TaskFilter
from django.utils.translation import gettext as _
from django.contrib import messages


# Create your views here.
class TaskIndexView(LoginRequiredMixin, View):
    login_url = 'login'
    template = 'tasks/index.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        statuses = Status.objects.all()
        executors = CustomUser.objects.all()
        labels = Label.objects.all()
        tasks_filtered = TaskFilter(
            request.GET, queryset=tasks, request=request
        )

        return render(
            request, self.template, {
                'statuses': statuses,
                'executors': executors,
                'labels': labels,
                'filter': tasks_filtered}
        )


class TaskShowView(View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)

        return render(request, 'tasks/show.html', context={
            'task': task,
            'task_id': task_id,
        })


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    success_message = _('Task is successfully created')

    template_name = 'tasks/create.html'
    model = Task
    fields = [
        'name',
        'description',
        'status',
        'executor',
        'labels',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task)

        return render(request, 'tasks/update.html', context={
            'form': form,
            'task_id': task_id,
        })

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task, data=request.POST)

        if form.is_valid():
            form.save()
            msg_text = _('Task is successfully updated')
            messages.success(request, msg_text)
            return redirect('task_index')

        return render(request, 'tasks/update.html', context={
            'form': form,
            'task_id': task_id,
        })


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'tasks/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)

        if request.user != task.author:
            msg_text = _('Only its author can delete a task')
            messages.error(request, msg_text)
            return redirect('task_index')
        msg_text = _('Task is successfully deleted')
        messages.success(request, msg_text)
        task.delete()
        return redirect('task_index')
