from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('sales.api.urls.sales_urls'))
]
