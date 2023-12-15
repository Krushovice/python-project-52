from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']


class CustomUserUpdateForm(CustomUserCreationForm):

    field_order = [
        'username',
        'first_name',
        'last_name',
    ]
