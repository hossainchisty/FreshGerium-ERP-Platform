from django.urls import path
from settings.views.password_change_views import passwordChangeView
from settings.views.settings_views import settings

urlpatterns = [
    path('', settings, name='settings'),
    path('password/change/', passwordChangeView, name='password_change'),
]
