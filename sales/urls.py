from django.urls import include, path

urlpatterns = [
    path('api/', include('sales.api.urls.sales_urls'))
]
