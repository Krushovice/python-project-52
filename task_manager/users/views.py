from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.utils.translation import gettext as _
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm


# Create your views here.
class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()[:15]
        user_logged_in = request.user.is_authenticated
        return render(request, 'users/index.html', context={
            'users': users,
            'user_logged_in': user_logged_in,
        })


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'users/create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg_text = _('User is successfully created')
            messages.success(request, msg_text)
            return redirect('login')
        return render(request, 'users/create.html', context={
            'form': form,
        })


class UserUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,

        }
        form = CustomUserUpdateForm(user=user, initial=initial_data)

        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        form = CustomUserUpdateForm(user=user,
                                    data=request.POST,
                                    instance=user)
        if form.is_valid():
            form.save()
            msg_text = _('User is successfully updated')
            messages.success(request, msg_text)
            return redirect('users_index')

        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })


class UserDeleteView(View):
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        if user:
            msg_text = _('User is successfully deleted')
            messages.success(request, msg_text)
            user.delete()
        return redirect('users_index')
