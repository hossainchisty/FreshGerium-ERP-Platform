from django.urls import path
from suppliers.views.suppliers_leader_views import SuppliersLedgerList
from suppliers.views.suppliers_list_views import SupplierList

urlpatterns = [
    path('', SupplierList.as_view(), name='suppliers_list'),
    path('ledger', SuppliersLedgerList.as_view(), name='suppliers_ledger_list'),
]
