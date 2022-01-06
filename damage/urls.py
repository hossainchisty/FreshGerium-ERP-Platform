from damage.views.add_manage_views import CreateDamage
from damage.views.damage_pdf_views import ViewDamagePDF
from damage.views.damange_manage_views import DamageList
from damage.views.delete_damage_views import DeleteDamage
from damage.views.download_damage_pdf import DownloadDamagePDF
from damage.views.export_damage_csv_views import DownloadDamageCSV
from damage.views.update_damage_views import UpdateDamage
from django.urls import path

urlpatterns = [
    path('', DamageList.as_view(), name='damage_list'),
    path('add/', CreateDamage.as_view(), name='add_damage'),
    path('update/<int:pk>/', UpdateDamage.as_view(), name='update_damage'),
    path('delete/<int:pk>/', DeleteDamage.as_view(), name='delete_damage'),
    path('export/', DownloadDamageCSV.as_view(), name='download_damage_csv'),
    path('pdf/', ViewDamagePDF.as_view(), name='view_damage_pdf'),
    path('pdf/download/', DownloadDamagePDF.as_view(), name='download_damage_pdf'),
]
