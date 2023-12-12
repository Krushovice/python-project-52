from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext as _
from django.contrib import messages
from .models import CustomUser
from .utils import UserAccessMixin
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


class UserUpdateView(UserAccessMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        form = CustomUserUpdateForm(user=user, instance=user)

        return render(request, 'users/update.html', context={
            'form': form,
            'user_id': user_id,
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
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


class UserDeleteView(UserAccessMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        return render(request, 'users/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_id)
        if user.author.exists() or user.executor.exists():
            msg_text = _('Cannot delete user because it is in use')
            messages.error(request, msg_text)
            return redirect('users_index')
        msg_text = _('User is successfully deleted')
        messages.success(request, msg_text)
        user.delete()
        return redirect('users_index')
