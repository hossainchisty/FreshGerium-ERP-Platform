from rest_framework import serializers
from .models import Opportunity



class OpportunitySerializer(serializers.ModelSerializer):

        class Meta:
            model = Opportunity
            fields = (  'id',
                        'name',
                        'Opportunities_description', 
                        'closed_on', 
                        'created_on',
                        'is_active',
                        'closed_by',
                        'contacts',
                        'accounts',
                        'teams',
                        )
            read_only_fields = (
                'Opportunities_description',
            ),



      


            