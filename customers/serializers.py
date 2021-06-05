from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'customer_name',
            'customer_email',
            'gender',
            'customer_address',
            'previous_balance',
            'accounts'
        )