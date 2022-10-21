from . models import Todoapp
from rest_framework import serializers

class TodoappSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Todoapp
        fields = [
            'title',
            'description',
            'status',
            'deadline',
            'color',
            'Is_important'
        ]
