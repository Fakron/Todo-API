from pipes import Template
from django.urls import path,include
from .views import (TodoListCreateview,TodoDetailView,)
from django.urls import re_path



urlpatterns = [
    path("",TodoListCreateview.as_view(),name="Todo-list"),
    path("<int:pk>/",TodoDetailView.as_view(),name="Todo-detail"),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
   
]
