from opportunities.models import Opportunity
from rest_framework import serializers


class OpportunitySerializer(serializers.ModelSerializer):
    '''
    Serializer for the opportunity model.
    '''
    class Meta:
        model = Opportunity
        fields = ('id', 'name', 'Opportunities_description', 'closed_on', 'created_on', 'is_active', 'closed_by', 'contacts', 'accounts', 'teams')
        read_only_fields = (
            'Opportunities_description',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True},
            'closed_on': {'required': False},
            'created_on': {'read_only': True},
        }
