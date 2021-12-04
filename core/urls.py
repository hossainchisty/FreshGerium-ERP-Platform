from core.views import core_views as views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
]
