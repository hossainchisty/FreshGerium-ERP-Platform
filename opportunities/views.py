from django.shortcuts import render
from rest_framework import generics
from .models import Opportunity
from .serializers import OpportunitySerializer
from rest_framework.permissions import IsAuthenticated


class OpportunityAPIView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all().order_by('-created_on')
    serializer_class = OpportunitySerializer

class CreateOpportunity(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class UpdateOpportunity(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class RetrieveOpportunity(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class DestroyOpportunity(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer