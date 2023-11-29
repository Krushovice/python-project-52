from django import forms
from .models import Status


class StatusCreationForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']


class StatusUpdateForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']
