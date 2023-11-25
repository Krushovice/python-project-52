from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from django.db import transaction
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
            return redirect('login')
        return render(request, 'users/create.html', context={
            'form': form,
        })


class UserUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        form = CustomUserUpdateForm(instance=user)

        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User was updated successfully')
            return redirect('users_index')
        else:
            messages.error(request, 'Can not update')
            return render(request, 'users/update.html', context={
                'form': form,
                'user_id': user_id,
            })


class UserDeleteView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
