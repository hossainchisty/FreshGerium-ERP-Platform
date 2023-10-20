from django.urls import path
from returns.views.return_view import ReturnView

urlpatterns = [
    path('', ReturnView.as_view(), name='return_list'),
]
