from rest_framework import serializers
from .models import Product,Order,Tag

class ProductSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Order
        fields = [
            'customer',
            'product',
            'status',
            'date_created',
        ]
        depth = 1