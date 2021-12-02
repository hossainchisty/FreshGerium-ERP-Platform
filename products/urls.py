from django.urls import path
from products.views import product_list_views as views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]
