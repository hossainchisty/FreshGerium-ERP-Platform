from django.urls import path
from returns.views.return_view import ReturnView
from returns.views.stock_return_list import StockReturnView
from returns.views.supplier_return_list import SupplierReturnView
from returns.views.wastage_return_list import WastageReturnView

urlpatterns = [
    path('', ReturnView.as_view(), name='return'),
    path('supplier/', SupplierReturnView.as_view(), name='supplier_return'),
    path('stock/', StockReturnView.as_view(), name='stock_return'),
    path('wastage/', WastageReturnView.as_view(), name='wastage_return'),
                          
]
