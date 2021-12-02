from django.urls import path
from suppliers.views import suppliers_list_views as views

urlpatterns = [
    path('', views.suppliers_list, name='suppliers_list'),
]
