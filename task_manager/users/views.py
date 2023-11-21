from django.shortcuts import render
from django.views import View
from .models import CustomUser as User


# Create your views here.
class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()[:15]
        return render(request, 'users/index.html', context={
            'users': users,
        })

    def post(self, request, *args, **kwargs):
        pass
