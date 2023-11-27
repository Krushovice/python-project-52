from django.contrib.auth.mixins import LoginRequiredMixin


class UserAccessMixin(LoginRequiredMixin):
    def check_user_access(self, user):
        if self.request.user.is_authenticated:
            # Получаем идентификатор пользователя из URL
            user_id = self.kwargs.get('pk')
            # Проверяем доступ текущего пользователя к профилю
            if self.request.user.id == user_id:
                return True  # У пользователя есть доступ к профилю
        return False  # У пользователя нет доступа к профилю
