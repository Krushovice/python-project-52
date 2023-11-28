from django.urls import path
from django.contrib.auth.decorators import login_required

from task_manager.users import views

urlpatterns = [
    path('', views.UsersIndexView.as_view(), name='users_index'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', login_required(views.UserUpdateView.as_view()),
         name='user_update'),
    path('<int:pk>/delete/', login_required(views.UserDeleteView.as_view()),
         name='user_delete'),

]
