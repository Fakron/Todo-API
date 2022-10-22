from rest_framework import generics
from .serializers import TodoappSerializers
from .models import Todoapp
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TodoListCreateview(generics.ListCreateAPIView):
    
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_important','status','color']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response = {
            'data':data,
            'count':len(data),
        }
        return Response(response)
    
    


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"





        

       
