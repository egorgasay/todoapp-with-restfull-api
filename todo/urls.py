from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from todo.views import *
from . import views


router = routers.DefaultRouter()
router.register(r'tasks', views.TodoTasksViewSet)
app_name = 'todo'
urlpatterns = [
    path('', include(router.urls)),
    path('create/', TodoCreateView.as_view()),
    path('tasks/all', TodoListView.as_view()),
    path('delete/<int:pk>/', DestroyView.as_view()),
    path('change-status/<int:pk>/', UpdateView.as_view()),
    path('id-info/', TodoIdsView.as_view()),
]
# path('all-tasks/', TodoListView.as_view()),
