from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    '''
    Serializer for Task model
    '''
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
