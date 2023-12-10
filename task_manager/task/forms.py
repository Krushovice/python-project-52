from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name']


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name']
