from .models import Todoapp
from rest_framework import serializers


class TodoappSerializers(serializers.ModelSerializer):
    isImportant = serializers.BooleanField(source='is_important')

    class Meta:
        model = Todoapp
        fields = (
            'id',
            'title',
            'description',
            'status',
            'deadline',
            'color',
            'isImportant',
            'created',
            'updated',
            'user_id'
        )
