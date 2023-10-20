from django.urls import path
from suppliers.views.add_supplier_views import AddSupplier
from suppliers.views.suppliers_list_views import SupplierList

urlpatterns = [
    path('list/', SupplierList.as_view(), name='suppliers_list'),
    path('add/', AddSupplier.as_view(), name='suppliers_add'),
]
