from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Status
from .forms import StatusCreationForm, StatusUpdateForm
from django.utils.translation import gettext as _
from django.contrib import messages


# Create your views here.
class StatusIndexView(View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()[:10]
        return render(request, 'statuses/index.html', context={
            'statuses': statuses
        })


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusCreationForm()
        return render(request, 'statuses/create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = StatusCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg_text = _('Status is successfully created')
            messages.success(request, msg_text)
            return redirect('status_index')
        return render(request, 'statuses/create.html', context={
            'form': form,
        })


class StatusUpdateView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_id)
        form = StatusUpdateForm(instance=status)

        return render(request, 'statuses/update.html', context={
            'form': form,
            'status_id': status_id,

        })

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_id)
        form = StatusUpdateForm(data=request.POST,
                                instance=status)
        if form.is_valid():
            form.save()
            msg_text = _('Status is successfully updated')
            messages.success(request, msg_text)
            return redirect('status_index')

        return render(request, 'statuses/update.html', context={
            'form': form,
            'status_id': status_id,
        })


class StatusDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_id)
        return render(request, 'statuses/index.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_id)
        if status:
            msg_text = _('Status is successfully deleted')
            messages.success(request, msg_text)
            status.delete()
        return redirect('status_index')
