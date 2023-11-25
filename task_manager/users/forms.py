from django.forms import ModelForm
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserUpdateForm(PasswordChangeForm, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
