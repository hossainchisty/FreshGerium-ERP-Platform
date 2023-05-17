from django.urls import include, path
from sales.views.add_sale_views import CreateSale
from sales.views.delete_sale_views import DeleteSale
from sales.views.download_sale_pdf import DownloadSalePDF
from sales.views.export_sale_csv_views import DownloadSaleCSV
from sales.views.manage_sale_views import SalesList
from sales.views.sale_pdf_views import ViewSalePDF
from sales.views.update_sale_views import UpdateSale
from sales.views.due_collection_views import DueCollection

urlpatterns = [
    path('', SalesList.as_view(), name='sales_list'),
    path('add/', CreateSale.as_view(), name='add_sales'),
    path('update/<int:pk>/', UpdateSale.as_view(), name='update_sale'),
    path('delete/<int:pk>/', DeleteSale.as_view(), name='delete_sale'),
    path('pdf/download/', DownloadSalePDF.as_view(), name="download_sale_pdf"),
    path('pdf/', ViewSalePDF.as_view(), name='view_sale_pdf'),
    path('export/', DownloadSaleCSV.as_view(), name="download_sale_csv"),
    path('due/', DueCollection.as_view(), name='due_collection'),
]
