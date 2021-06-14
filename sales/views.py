from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
) 
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Product,Order
from .throttling import ProductRateThrottle
from .serializers import ProductSerializer,OrderSerializer


class ProductAPIView(ListAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    throttle_classes = [ProductRateThrottle,AnonRateThrottle]
    # ordering_fields = ['Name']

class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DestroyProduct(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

'''
'''
class OrderAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]

class CreateOrder(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]

class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle,AnonRateThrottle]

class RetrieveOrder(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle,AnonRateThrottle]

class DestroyOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    throttle_classes = [UserRateThrottle,AnonRateThrottle]