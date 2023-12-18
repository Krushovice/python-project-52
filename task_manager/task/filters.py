import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request, 'user', None)

        return parent.filter(author=author)
