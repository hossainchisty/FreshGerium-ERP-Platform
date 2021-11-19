from django.shortcuts import render
from .models import Leads
from .serializers import LeadSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class LeadAPIList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all().order_by('-created_on')
    serializer_class = LeadSerializers

class CreateLead(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers

class UpdateLead(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers

class RetrieveLead(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers

class DestroyLead(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Leads.objects.all()
    serializer_class = LeadSerializers
