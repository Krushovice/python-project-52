from django import forms
from .models import Label


class LabelCreationForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']


class LabelUpdateForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']
