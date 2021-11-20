from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from customers.api.serializers.customer_serializers import CustomerSerializer
from customers.models import Customer


class CustomerList(generics.ListAPIView):
    '''
    ♻API endpoint that allows customers to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all().order_by("-id")
    serializer_class = CustomerSerializer


class CreateCustomer(generics.CreateAPIView):
    '''
    ♻API endpoint that allows customers to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UpdateCustomer(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows customers to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RetrieveCustomer(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows customers to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DestroyCustomer(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows customers to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
