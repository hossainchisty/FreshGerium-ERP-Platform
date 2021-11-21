from rest_framework import serializers
from sales.models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    '''
    Serializer for Product model
    '''
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'quantity',
            'tags',
            'category',
            'description',
            'date_created',
        )
        read_only_fields = ('date_created',)
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    '''
    Serializer for Order model
    '''
    class Meta:
        model = Order
        fields = [
            'customer',
            'product',
            'status',
            'date_created',
        ]
        depth = 1
