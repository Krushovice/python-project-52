from django.urls import path

from task_manager.tasks.views import IndexView, TaskView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', TaskView.as_view(), name='task_show'),
]
