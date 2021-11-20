from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    '''
    Serializer for Account model
    '''
    class Meta:
        model = Account
        fields = ('user', 'account_name', 'account_description', 'country', 'account_phone',  'billing_address', 'organization_industry')
