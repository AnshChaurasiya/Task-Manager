
from django.contrib import admin
from django.urls import path, include
from todolist import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task/', views.tasklist, name="tasklist"),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete_uncomplete/<task_id>', views.complete_uncomplete_task, name='complete_uncomplete_task'),
]
