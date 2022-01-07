from django.urls import path
from purchase.views.add_purchase_views import CreatePurchase
from purchase.views.delete_purchase_views import DeletePurchase
from purchase.views.download_purchase_pdf import DownloadPurchasePDF
from purchase.views.export_purchase_csv_views import DownloadPurchaseCSV
from purchase.views.export_purchase_excle_views import DownloadPurchaseEXCLE
from purchase.views.manage_purchase_views import ManagePurchase
from purchase.views.purchase_pdf_views import ViewPurchasePDF
from purchase.views.update_purchase_views import UpdatePurchase

urlpatterns = [
    path('manage/', ManagePurchase.as_view(), name='manage_purchase'),
    path('add/', CreatePurchase.as_view(), name='add_purchase'),
    path('delete/<int:pk>/', DeletePurchase.as_view(), name='delete_purchase'),
    path('update/<int:pk>/', UpdatePurchase.as_view(), name='update_purchase'),
    path('export/excle/', DownloadPurchaseEXCLE.as_view(), name='download_purchase_excle'),
    path('export/csv/', DownloadPurchaseCSV.as_view(), name='download_purchase_csv'),
    path('pdf/', ViewPurchasePDF.as_view(), name='view_purchase_pdf'),
    path('pdf/download/', DownloadPurchasePDF.as_view(), name="download_purchase_pdf")
]
