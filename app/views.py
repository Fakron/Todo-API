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



class TodoDetailsViewAPI(generics.RetrieveAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers


class TodoUpdateViewAPI(generics.UpdateAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class TodoDeleteViewAPI(generics.DestroyAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"





        

       
