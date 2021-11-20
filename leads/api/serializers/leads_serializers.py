from rest_framework import serializers

from leads.models import Leads


class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'data_of_birth',
            'source',
            'assigned_to',
            'status',
            'country',
            'zipcode',
            'website',
            'description',
            'contacts',
            'teams',
            'accounts_name',
            'created_by',
            'created_on',
            'is_active',
        )
