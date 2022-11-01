from rest_framework import generics
from .serializers import TodoappSerializers
from .models import Todoapp
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import date
import jwt
from django.conf import settings


# Create your views here.

class TodoListCreateview(generics.ListCreateAPIView):
    queryset = Todoapp.objects.all().order_by('-created')
    serializer_class = TodoappSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_important', 'status', 'color', 'deadline', 'user_id']
    permission_classes = [permissions.IsAuthenticated]

    # decoding the token

    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token['user_id']
        request.data['user_id'] = user_id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):

        # decoding the token
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token['user_id']
        queryset = self.filter_queryset(self.get_queryset().filter(user_id=user_id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        response = {
            'data': data,
            'count': len(data),

        }
        return Response(response)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = TodoappSerializers
    lookup_field = "pk"
