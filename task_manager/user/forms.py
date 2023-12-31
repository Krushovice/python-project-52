from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class CustomUserUpdateForm(CustomUserCreationForm):

    field_order = [
        'first_name',
        'last_name',
        'username',
    ]
