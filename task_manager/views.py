from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):
    """Root index view for Anonumus and Logged user."""
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(SuccessMessageMixin, LoginView):
    """User login page view."""
    template_name = 'users/login.html'
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
