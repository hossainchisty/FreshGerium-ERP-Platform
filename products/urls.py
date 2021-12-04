from django.urls import path
from products.views.product_list_views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
]
