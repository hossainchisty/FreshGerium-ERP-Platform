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
        depth = 1
        # read_only_fields = ()

class OrderSerializer(serializers.ModelSerializer):
    models = Order
    fields = (
        'id',
        'customer',
        'product',
        'status',
        'date_created',
    )