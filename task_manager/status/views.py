from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views import View
from .models import Status


# Create your views here.
class StatusIndexView(View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()[:10]
        return render(request, 'statuses/index.html', context={
            'statuses': statuses
        })


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class StatusDeleteView(View):
    def post(self, request, *args, **kwargs):
        pass
