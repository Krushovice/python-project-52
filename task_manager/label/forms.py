from django import forms
from .models import Label


class StatusCreationForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']


class StatusUpdateForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']
