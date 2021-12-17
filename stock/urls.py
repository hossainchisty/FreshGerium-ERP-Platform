from django.urls import path
from stock.views.export_stock_csv_views import DownloadStockCSV
from stock.views.stock_report_views import StockReportView
from stock.views.stock_pdf_views import ViewStockPDF

urlpatterns = [
    path('report/', StockReportView.as_view(), name='stock_report'),
    path('export/', DownloadStockCSV.as_view(), name='donwload_stock_csv'),
    path('pdf/', ViewStockPDF.as_view(), name='view_stock_pdf'),
]
