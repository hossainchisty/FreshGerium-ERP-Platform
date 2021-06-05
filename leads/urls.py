from django.urls import path

from . views import (
    LeadAPIList,
    CreateLead,
    UpdateLead,
    RetrieveLead,
    DestroyLead,
)

urlpatterns = [
    path('list/', LeadAPIList.as_view()),
    path('create/', CreateLead.as_view()),
    path('update/<int:pk>/', UpdateLead.as_view()),
    path('retrieve/<int:pk>/', RetrieveLead.as_view()), 
    path('destory/<int:pk>/', DestroyLead.as_view())                          
]

'''
#? API endpoint of tasks
http://127.0.0.1:8000/leads/list/
http://127.0.0.1:8000/leads/create
http://127.0.0.1:8000/leads/update/<int:pk>/
http://127.0.0.1:8000/leads/retrieve/<int:pk>/
http://127.0.0.1:8000/leads/destory/<int:pk>/
'''