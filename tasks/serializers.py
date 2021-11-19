from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'status',
            'priority',
            'due_date',
            'created_on',
            'account',
            'contact',
            'assigned_to',
            'teams',
        )