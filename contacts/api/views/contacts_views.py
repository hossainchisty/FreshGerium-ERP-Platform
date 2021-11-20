from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from contacts.api.serializers.contacts_serializers import ContactSerializer
from contacts.models import Contact


class ContactList(generics.ListAPIView):
    '''
    ♻API endpoint that allows contact to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all().order_by('created_on')
    serializer_class = ContactSerializer


class CreateContact(generics.CreateAPIView):
    '''
    ♻API endpoint that allows contact to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UpdateContact(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows contact to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class RetrieveContact(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows contact to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DestroyContact(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows contact to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
