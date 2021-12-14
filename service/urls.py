from django.urls import path
from service.views.add_service_views import CreateService
from service.views.delete_service_views import DeleteService
from service.views.manage_service_views import ManageService
from service.views.update_service_views import ServiceUpdate

urlpatterns = [
    path('manage/', ManageService.as_view(), name='manage_service'),
    path('add/', CreateService.as_view(), name='add_service'),
    path('update/<pk>/', ServiceUpdate.as_view(), name='update_service'),
    path('delete/<pk>/', DeleteService.as_view(), name='delete_service'),
]
