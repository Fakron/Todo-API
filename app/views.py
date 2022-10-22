from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoappSerializers
from .models import Todoapp
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class TodoListCreateview(generics.ListCreateAPIView):
    
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Is_important']


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"





        

       
