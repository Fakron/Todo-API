from pipes import Template
from django.urls import path,include
from .views import (TodoListCreateview,TodoDetailsViewAPI,TodoUpdateViewAPI,TodoDeleteViewAPI)

urlpatterns = [
    path("",TodoListCreateview.as_view(),name="Todo-list"),
    
    path("<int:pk>/update",TodoUpdateViewAPI.as_view(),name="Todo-update"),
    path("<int:pk>/delete",TodoDeleteViewAPI.as_view(),name="Todo-delete"),
    path("<int:pk>",TodoDetailsViewAPI.as_view(),name="Todo-detail"),
    
]
