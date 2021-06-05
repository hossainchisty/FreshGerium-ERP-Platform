from django.shortcuts import render
from .models import Contact
from rest_framework import generics
from .serializers import ContactSerializer


class ContactList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all().order_by('created_on')
    serializer_class = ContactSerializer

class CreateContact(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class UpdateContact(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class RetrieveContact(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class DestroyContact(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

