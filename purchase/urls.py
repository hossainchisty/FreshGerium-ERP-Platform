from django.urls import path
from purchase.views.add_purchase_views import CreatePurchase
from purchase.views.delete_purchase_views import DeletePurchase
from purchase.views.manage_purchase_views import ManagePurchase
from purchase.views.update_purchase_views import UpdatePurchase

urlpatterns = [
    path('manage/', ManagePurchase.as_view(), name='manage_purchase'),
    path('add/', CreatePurchase.as_view(), name='add_purchase'),
    path('delete/<int:pk>/', DeletePurchase.as_view(), name='delete_purchase'),
    path('update/<int:pk>/', UpdatePurchase.as_view(), name='update_purchase'),
]
