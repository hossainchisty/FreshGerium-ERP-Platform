from django.urls import path
from purchase.views.manage_purchase_views import ManagePurchase

urlpatterns = [
    path('manage/', ManagePurchase.as_view(), name='manage_purchase'),
]
