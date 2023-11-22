from django.shortcuts import render, redirect
from django.views import View
# from django.db import transaction
from .models import User
from .forms import UserCreationForm, UserUpdateForm


# Create your views here.
class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()[:15]
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'users/create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_index')


class UserUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(instance=user)

        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_index')


class UserDeleteView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
