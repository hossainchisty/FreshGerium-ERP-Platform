from core.views.core_views import Dashboard
from django.urls import path

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
