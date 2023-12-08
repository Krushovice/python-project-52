from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views import View
from .models import Label


# Create your views here.Label
class LabelIndexView(View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()[:10]
        return render(request, 'labels/index.html', context={
            'labels': labels
        })


class LabelCreateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class LabelUpdateView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class LabelDeleteView(View):
    def post(self, request, *args, **kwargs):
        pass
