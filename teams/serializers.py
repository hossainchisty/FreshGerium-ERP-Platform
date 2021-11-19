from rest_framework import serializers
from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
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