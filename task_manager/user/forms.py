from django import forms
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserUpdateForm(PasswordChangeForm, forms.ModelForm):

    def __init__(self, *, user, **kwargs):
        super().__init__(user, **kwargs)

    field_order = [
        'first_name',
        'last_name',
        'username',
        'old_password',
        'new_password1',
        'new_password2',
    ]

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']
