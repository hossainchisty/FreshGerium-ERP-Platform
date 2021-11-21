from rest_framework import serializers
from teams.models import Teams


class TeamSerializer(serializers.ModelSerializer):
    '''
    Serializer for Teams model
    '''
    class Meta:
        model = Teams
        fields = (
            'id',
            'users',
            'name',
            'description',
            'created_on',
            'created_by',
        )
