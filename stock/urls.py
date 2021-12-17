from django.urls import path
from stock.views.export_stock_csv_views import DownloadStockCSV
from stock.views.stock_report_views import StockReportView

urlpatterns = [
    path('report/', StockReportView.as_view(), name='stock_report'),
    path('export/', DownloadStockCSV.as_view(), name='donwload_stock_csv'),
]
