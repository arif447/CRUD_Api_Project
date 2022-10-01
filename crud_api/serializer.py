from rest_framework import serializers
from . models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'Description', 'create_at', 'completed')
