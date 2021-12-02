from django.urls import path
from sales.api.views import sales_views as views

urlpatterns = [
    path('sale/list/', views.SaleAPIView.as_view()),
    path('sale/create/', views.CreateSale.as_view()),
    path('sale/update/<int:pk>/', views.UpdateSale.as_view()),
    path('sale/retrieve/<int:pk>/', views.RetrieveSale.as_view()),
    path('sale/destory/<int:pk>/', views.DestroySale.as_view()),
]
