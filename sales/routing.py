from django.urls import path
from sales.consumers import SaleGraphConsumer

ws_urlpatterns = [
    path('ws/sales/graph/', SaleGraphConsumer.as_asgi()),
]
