from django.urls import path

from . views import (

    ProductAPIView,
    CreateProduct,
    UpdateProduct,
    RetrieveProduct,
    DestroyProduct,

    OrderAPIView,
    CreateOrder,
    UpdateOrder,
    RetrieveOrder,
    DestroyOrder,
)

urlpatterns = [

    path('product/list/', ProductAPIView.as_view()),
    path('product/create/', CreateProduct.as_view()),
    path('product/update/<int:pk>/', UpdateProduct.as_view()),
    path('product/retrieve/<int:pk>/', RetrieveProduct.as_view()), 
    path('product/destory/<int:pk>/', DestroyProduct.as_view()),

    path('order/list/', OrderAPIView.as_view()),
    path('order/create/', CreateOrder.as_view()),
    path('order/update/<int:pk>/', UpdateOrder.as_view()),
    path('order/retrieve/<int:pk>/', RetrieveOrder.as_view()), 
    path('order/destory/<int:pk>/', DestroyOrder.as_view()),

                          
]

'''
#? API endpoint of sales ,product 
http://127.0.0.1:8000/sales/product/list/
http://127.0.0.1:8000/sales/product/create
http://127.0.0.1:8000/sales/product/update/<int:pk>/
http://127.0.0.1:8000/sales/product/retrieve/<int:pk>/
http://127.0.0.1:8000/sales/product/destory/<int:pk>/

#? API endpoint of sales ,order
http://127.0.0.1:8000/sales/order/list/
http://127.0.0.1:8000/sales/order/create
http://127.0.0.1:8000/sales/order/update/<int:pk>/
http://127.0.0.1:8000/sales/order/retrieve/<int:pk>/
http://127.0.0.1:8000/sales/order/destory/<int:pk>/
'''