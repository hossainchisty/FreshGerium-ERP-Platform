from order.views.add_manage_views import CreateOrder
from order.views.order_pdf_views import ViewOrderPDF
from order.views.order_manage_views import OrderList
from order.views.delete_oder_views import DeleteOrder
from order.views.download_order_pdf import DownloadOrderPDF
from order.views.export_order_csv_views import DownloadDamageCSV
from order.views.export_order_excle_views import DownloadDamageEXCLE
from order.views.update_order_views import UpdateOrder
from django.urls import path

urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('add/', CreateOrder.as_view(), name='add_order'),
    path('update/<int:pk>/', UpdateOrder.as_view(), name='update_order'),
    path('delete/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('export/excle/', DownloadDamageEXCLE.as_view(), name='download_order_excle'),
    path('export/csv/', DownloadDamageCSV.as_view(), name='download_order_csv'),
    path('pdf/', ViewOrderPDF.as_view(), name='view_order_pdf'),
    path('pdf/download/', DownloadOrderPDF.as_view(), name='download_order_pdf'),
]
