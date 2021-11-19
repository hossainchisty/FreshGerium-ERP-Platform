from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "customer_name",
            "customer_email",
            "gender",
            "customer_address",
            "previous_balance",
            "accounts",
        )

    # Object-level validation
    def validate(self, data):
        if len(data["customer_name"]) < 8:
            raise serializers.ValidationError("Name should be at least 8 characters")
        return data
