from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from customers.api.serializers.customer_serializers import CustomerSerializer
from customers.models import Customer


class CustomerList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all().order_by("-id")
    serializer_class = CustomerSerializer


class CreateCustomer(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class UpdateCustomer(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RetrieveCustomer(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DestroyCustomer(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
