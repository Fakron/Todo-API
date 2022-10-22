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
    filterset_fields = ['is_important']

    #object count
    def get(self, request, format=None):
        rs = Todoapp.objects.all()
        is_important = Todoapp.objects.filter(is_important=True)
        serializer = TodoappSerializers(rs, many=True)
        return Response({"data": serializer.data, "totalCount": len(rs),"totalIsImportant":len(is_important)}, status=status.HTTP_200_OK)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"





        

       
