from opportunities.api.serializers.opportunity_serializers import (
    OpportunitySerializer,
)
from opportunities.models import Opportunity
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class OpportunityAPIView(generics.ListAPIView):
    '''
    ♻API endpoint that allows opportunity to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all().order_by('-created_on')
    serializer_class = OpportunitySerializer


class CreateOpportunity(generics.CreateAPIView):
    '''
    ♻API endpoint that allows opportunity to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class UpdateOpportunity(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows opportunity to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class RetrieveOpportunity(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows opportunity to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer


class DestroyOpportunity(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows opportunity to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
