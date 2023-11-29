from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext as _


class UserAccessMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        user_id = self.kwargs.get('pk')
        return self.request.user.pk == user_id

    def handle_no_permission(self):
        msg_text = _("You don't have permition to change other user")
        messages.error(self.request, msg_text)
        return redirect('users_index')
