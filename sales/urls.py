from django.urls import include, path
from sales.views import sales_list_views as views

urlpatterns = [
    path('api/v1/', include('sales.api.urls.sales_urls')),
    path('', views.sales_list, name='sales_list'),
]
