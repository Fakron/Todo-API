from pipes import Template
from django.urls import path
from .views import (TodoListCreateview, TodoDetailView, )

urlpatterns = [
    path("todo/", TodoListCreateview.as_view(), name="Todo-list"),
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="Todo-detail"),
]
