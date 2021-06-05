from django.urls import path

from . views import (

    CustomerList,
    CreateCustomer,
    UpdateCustomer,
    RetrieveCustomer,
    DestroyCustomer,
)

urlpatterns = [
    path('list/', CustomerList.as_view()),
    path('create/', CreateCustomer.as_view()),
    path('update/<int:pk>/', UpdateCustomer.as_view()),
    path('retrieve/<int:pk>/', RetrieveCustomer.as_view()), 
    path('destory/<int:pk>/', DestroyCustomer.as_view())                          
]

'''
#? API endpoint of opportunity
http://127.0.0.1:8000/customers/list/
http://127.0.0.1:8000/customers/create
http://127.0.0.1:8000/customers/update/<int:pk>/
http://127.0.0.1:8000/customers/retrieve/<int:pk>/
http://127.0.0.1:8000/customers/destory/<int:pk>/
'''