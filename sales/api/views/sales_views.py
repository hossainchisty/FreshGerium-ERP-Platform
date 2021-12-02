from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly,
)
from rest_framework.throttling import AnonRateThrottle

from sales.api.serializers.sales_serializers import SaleSerializer
from sales.models import Sale
from sales.throttling import SaleRateThrottle


class SaleAPIView(ListAPIView):
    '''
    ♻API endpoint that allows Sale to be viewed.
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    throttle_classes = [SaleRateThrottle, AnonRateThrottle]
    ordering_fields = ['Name']


class CreateSale(CreateAPIView):
    '''
    ♻API endpoint that allows Sale to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class UpdateSale(UpdateAPIView):
    '''
    ♻API endpoint that allows Sale to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class RetrieveSale(RetrieveAPIView):
    '''
    ♻API endpoint that allows Sale to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class DestroySale(DestroyAPIView):
    '''
    ♻API endpoint that allows Sale to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
