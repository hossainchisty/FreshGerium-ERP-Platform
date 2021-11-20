from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'first_name',
            'last_name',
            'accounts',
            'email',
            'phone_number',
            'address',
            'created_by',
            'created_on',
            'is_active',
        )
