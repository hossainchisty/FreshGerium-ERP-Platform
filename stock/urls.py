from django.urls import path
from stock.views.stock_report_views import StockReportView

urlpatterns = [
    path('report/', StockReportView.as_view(), name='stock_report'),
]
