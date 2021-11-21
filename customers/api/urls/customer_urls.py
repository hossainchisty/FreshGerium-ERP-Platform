from customers.api.views import customer_views as views
from django.urls import path

urlpatterns = [
    path('list/', views.CustomerList.as_view()),
    path('create/', views.CreateCustomer.as_view()),
    path('update/<int:pk>/', views.UpdateCustomer.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveCustomer.as_view()),
    path('destory/<int:pk>/', views.DestroyCustomer.as_view()),
]
