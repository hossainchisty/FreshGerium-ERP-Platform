from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    '''
    Serializer for Sale model
    '''
    class Meta:
        model = Sale
        fields = '__all__'
        read_only_fields = ('date_created',)
        depth = 1
