from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from leads.api.serializers.leads_serializers import LeadSerializers
from leads.models import Leads


class LeadAPIList(generics.ListAPIView):
    '''
    ♻API endpoint that allows leads to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all().order_by('-created_on')
    serializer_class = LeadSerializers


class CreateLead(generics.CreateAPIView):
    '''
    ♻API endpoint that allows leads to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers


class UpdateLead(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows leads to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers


class RetrieveLead(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows leads to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers


class DestroyLead(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows leads to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers
