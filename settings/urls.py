from django.urls import path
from settings.views import settings_views as views

urlpatterns = [
    path('', views.settings, name='settings'),
]
