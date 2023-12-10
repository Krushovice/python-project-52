from django.urls import path

from task_manager.task import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='task_index'),
    path('<int:pk>/', views.TaskShowView.as_view(), name='task_show'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(),
         name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(),
         name='task_delete'),

]
