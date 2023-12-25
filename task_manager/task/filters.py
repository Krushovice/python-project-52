import django_filters
from .models import Task
from task_manager.user.models import CustomUser as User
from task_manager.status.models import Status
from task_manager.label.models import Label


class TaskFilter(django_filters.FilterSet):
    author = django_filters.ModelChoiceFilter(field_name='author',
                                              queryset=User.objects.all())
    status = django_filters.ModelChoiceFilter(field_name='status',
                                              queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(field_name='executor',
                                                queryset=User.objects.all())
    labels = django_filters.ModelMultipleChoiceFilter(field_name='labels',
                                                      queryset=Label.objects.all())  # noqa

    class Meta:
        model = Task
        fields = ['name', 'author', 'status', 'executor', 'labels']

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        user = getattr(self.request, 'user', None)
        it_self = self.request.GET.get('self_tasks', None)

        if user and user.is_authenticated:
            if it_self:
                queryset = queryset.filter(author=user)

        return queryset
