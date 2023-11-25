from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       AuthenticationForm)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']
