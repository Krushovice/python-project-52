from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('index')
    success_message = _("You are logged in")


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        msg_text = _("You are logged out")
        messages.info(self.request, msg_text)
        return response
