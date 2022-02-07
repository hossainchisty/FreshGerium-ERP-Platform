from django.urls import path
from profiles.views.data_download_views import data_download
from profiles.views.password_verification_views import password_verification
from profiles.views.profile_views import profile

urlpatterns = [
    path('', profile, name='profile'),
    path('download/request/', data_download, name='data_download'),
    path('verification/', password_verification, name='password_verification'),
]
