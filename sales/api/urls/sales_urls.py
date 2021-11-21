from django.urls import path
from sales.api.views import sales_views as views

urlpatterns = [
    path('product/list/', views.ProductAPIView.as_view()),
    path('product/create/', views.CreateProduct.as_view()),
    path('product/update/<int:pk>/', views.UpdateProduct.as_view()),
    path('product/retrieve/<int:pk>/', views.RetrieveProduct.as_view()),
    path('product/destory/<int:pk>/', views.DestroyProduct.as_view()),
    path('order/list/', views.OrderAPIView.as_view()),
    path('order/create/', views.CreateOrder.as_view()),
    path('order/update/<int:pk>/', views.UpdateOrder.as_view()),
    path('order/retrieve/<int:pk>/', views.RetrieveOrder.as_view()),
    path('order/destory/<int:pk>/', views.DestroyOrder.as_view()),
]
