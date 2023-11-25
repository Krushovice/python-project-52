from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, LoginView, LogoutView
# from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginView(SuccessMessageMixin, LoginView):
    """User login page view."""
    template_name = 'user/login.html'
    next_page = reverse_lazy('index')
    success_message = _("You are logged in")
    # def get(self, request, *args, **kwargs):
    #     form = CustomUserLoginForm()
    #     return render(request, 'login.html', {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = CustomUserLoginForm(request, data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         messages.success(request, 'User was logged in successfully')
    #         return redirect('index')
    #     else:
    #         form = CustomUserLoginForm()
    #         messages.error(request, 'Check username or password')
    #         return render(request, 'login.html', {'form': form})
