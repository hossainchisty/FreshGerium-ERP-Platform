from customers.api.views import customer_views
from django.urls import path

urlpatterns = [
    path('list/', customer_views.CustomerList.as_view()),
    path('create/', customer_views.CreateCustomer.as_view()),
    path('update/<int:pk>/', customer_views.UpdateCustomer.as_view()),
    path('retrieve/<int:pk>/', customer_views.RetrieveCustomer.as_view()),
    path('destory/<int:pk>/', customer_views.DestroyCustomer.as_view()),
]

'''
#? API endpoint of opportunity
http://127.0.0.1:8000/customers/list/
http://127.0.0.1:8000/customers/create
http://127.0.0.1:8000/customers/update/<int:pk>/
http://127.0.0.1:8000/customers/retrieve/<int:pk>/
http://127.0.0.1:8000/customers/destory/<int:pk>/
'''
