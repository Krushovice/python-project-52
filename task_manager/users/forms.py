from django.forms import ModelForm
from .models import User


class UserCreationForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class UserLoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
