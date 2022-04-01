from analytics.views.customer_graph_views import CustomerGraphViews
from django.urls import path

urlpatterns = [
    path('customer/graph/', CustomerGraphViews.as_view(), name='customer_graph')
]
