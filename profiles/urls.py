from django.urls import path
from profiles.views.data_download_views import data_download
from profiles.views.data_views import data_view
from profiles.views.download_confirm_views import download_confirm
from profiles.views.download_requested_views import download_requested
from profiles.views.password_verification_views import password_verification
from profiles.views.profile_views import profile

urlpatterns = [
    path('', profile, name='profile'),
    path('download/request/', data_download, name='data_download'),
    path('verification/', password_verification, name='password_verification'),
    path('download/requested/', download_requested, name='data_download_requested'),
    path('download/confirm/', download_confirm, name='download_confirm'),
    path('data/', data_view, name='data_view'),
]
