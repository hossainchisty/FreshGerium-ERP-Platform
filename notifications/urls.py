from django.urls import path
from notifications.views.notifications_views import NotificationView

urlpatterns = [
    path('', NotificationView.as_view(), name='notifications'),
]
