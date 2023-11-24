from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
# from django.db import transaction
from django.contrib import messages
from task_manager.users.forms import UserLoginForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginView(View):
    def get(self, request, *args, **kwargs):
        # Получение данных из сессии, если они доступны
        username = request.session.get('username')
        password = request.session.get('password')

        form = UserLoginForm(initial={'username': username, 'password': password})
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'User was logged in successfully')
            return redirect('index')
        else:
            form = UserLoginForm()
            messages.error(request, 'Check username or password')
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('index')
