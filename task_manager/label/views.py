from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .models import Label
from .forms import LabelCreationForm, LabelUpdateForm
from django.utils.translation import gettext as _
from django.contrib import messages


# Create your views here.Label
class LabelIndexView(View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()[:10]
        return render(request, 'labels/index.html', context={
            'labels': labels
        })


class LabelCreateView(View):
    def get(self, request, *args, **kwargs):
        form = LabelCreationForm()
        return render(request, 'labels/create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = LabelCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg_text = _('Label is successfully created')
            messages.success(request, msg_text)
            return redirect('labels_index')
        return render(request, 'labels/create.html', context={
            'form': form,
        })


class LabelUpdateView(View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_id)
        form = LabelUpdateForm(instance=label)

        return render(request, 'labels/update.html', context={
            'form': form,
            'label_id': label_id,
        })

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_id)
        form = LabelUpdateForm(data=request.POST,
                               instance=label)
        if form.is_valid():
            form.save()
            msg_text = _('Label is successfully updated')
            messages.success(request, msg_text)
            return redirect('labels_index')

        return render(request, 'labels/update.html', context={
            'form': form,
            'label_id': label_id,
        })


class LabelDeleteView(View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_id)
        return render(request, 'labels/delete.html', {'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_id)
        # Проверяем, есть ли связанные задачи
        if label.tasks.exists():
            msg_text = _('Cannot delete label because it is in use')
            messages.error(request, msg_text)
            return redirect('label_index')
        msg_text = _('Label is successfully deleted')
        messages.success(request, msg_text)
        label.delete()
        return redirect('label_index')
