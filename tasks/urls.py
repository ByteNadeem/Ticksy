from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:task_id>/toggle/', views.task_toggle_complete, name='task_toggle_complete'),
]
