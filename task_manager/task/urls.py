from django.urls import path

from task_manager.task import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:id>/', views.TaskView.as_view(), name='task_show'),
]
