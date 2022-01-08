from django.urls import path
from service.views.add_service_views import CreateService
from service.views.delete_service_views import DeleteService
from service.views.download_service_pdf import DownloadServicePDF
from service.views.export_service_csv_views import DownloadServiceCSV
from service.views.export_service_excle_views import DownloadServiceEXCLE
from service.views.manage_service_views import ManageService
from service.views.service_pdf_views import ViewServicePDF
from service.views.update_service_views import ServiceUpdate

urlpatterns = [
    path('manage/', ManageService.as_view(), name='manage_service'),
    path('add/', CreateService.as_view(), name='add_service'),
    path('update/<pk>/', ServiceUpdate.as_view(), name='update_service'),
    path('delete/<pk>/', DeleteService.as_view(), name='delete_service'),
    path('export/excle/', DownloadServiceEXCLE.as_view(), name='download_service_excle'),
    path('export/csv/', DownloadServiceCSV.as_view(), name='download_service_csv'),
    path('pdf/', ViewServicePDF.as_view(), name='view_service_pdf'),
    path('pdf/download/', DownloadServicePDF.as_view(), name='download_service_pdf'),
]
