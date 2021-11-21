from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly,
)
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from sales.api.serializers.sales_serializers import (
    OrderSerializer, ProductSerializer,
)
from sales.models import Order, Product
from sales.throttling import ProductRateThrottle


class ProductAPIView(ListAPIView):
    '''
    ♻API endpoint that allows product to be viewed.
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    throttle_classes = [ProductRateThrottle, AnonRateThrottle]
    ordering_fields = ['Name']


class CreateProduct(CreateAPIView):
    '''
    ♻API endpoint that allows product to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProduct(UpdateAPIView):
    '''
    ♻API endpoint that allows product to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProduct(RetrieveAPIView):
    '''
    ♻API endpoint that allows product to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DestroyProduct(DestroyAPIView):
    '''
    ♻API endpoint that allows product to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderAPIView(ListAPIView):
    '''
    ♻API endpoint that allows order to be viewed.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class CreateOrder(CreateAPIView):
    '''
    ♻API endpoint that allows order to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class UpdateOrder(UpdateAPIView):
    '''
    ♻API endpoint that allows order to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class RetrieveOrder(RetrieveAPIView):
    '''
    ♻API endpoint that allows order to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class DestroyOrder(DestroyAPIView):
    '''
    ♻API endpoint that allows order to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
