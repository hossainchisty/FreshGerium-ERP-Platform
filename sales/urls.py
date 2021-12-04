from django.urls import include, path
from sales.views import manage_sale_views as views

urlpatterns = [
    path('api/v1/', include('sales.api.urls.sales_urls')),
    path('', views.SalesList.as_view(), name='sales_list'),
]
