from django.urls import path

from . views import (

    OpportunityAPIView,
    CreateOpportunity,
    UpdateOpportunity,
    RetrieveOpportunity,
    DestroyOpportunity,
)

urlpatterns = [
    path('list/', OpportunityAPIView.as_view()),
    path('create/', CreateOpportunity.as_view()),
    path('update/<int:pk>/', UpdateOpportunity.as_view()),
    path('retrieve/<int:pk>/', RetrieveOpportunity.as_view()), 
    path('destory/<int:pk>/', DestroyOpportunity.as_view())                          
]

'''
#? API endpoint of opportunity
http://127.0.0.1:8000/opportunity/list/
http://127.0.0.1:8000/opportunity/create
http://127.0.0.1:8000/opportunity/update/<int:pk>/
http://127.0.0.1:8000/opportunity/retrieve/<int:pk>/
http://127.0.0.1:8000/opportunity/destory/<int:pk>/
'''