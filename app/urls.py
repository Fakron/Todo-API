from pipes import Template
from django.urls import path
from .views import (TodoListCreateview,TodoDetailView,)

urlpatterns = [
    path("",TodoListCreateview.as_view(),name="Todo-list"),
    path("<int:pk>/",TodoDetailView.as_view(),name="Todo-detail"),
]
