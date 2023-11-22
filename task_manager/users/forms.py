from django.forms import ModelForm
from .models import User


class CustomUserCreationForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'pswrd']


class CustomUserChangeForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'pswrd']
