from authenticator.views.logout_views import LogoutView

from django.urls import path

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]
