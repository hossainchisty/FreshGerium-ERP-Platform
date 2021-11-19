from django.urls import path

from . views import (
   TeamAPIList,
   CreateTeam,
    UpdateTeam,
    RetrieveTeam,
    DestroyTeam,

)

urlpatterns = [
    path('list/', TeamAPIList.as_view()),
    path('create/', CreateTeam.as_view()),
    path('update/<int:pk>/', UpdateTeam.as_view()),
    path('retrieve/<int:pk>/', RetrieveTeam.as_view()), 
    path('destory/<int:pk>/', DestroyTeam.as_view())                          
]

'''
#? API endpoint of teams
http://127.0.0.1:8000/teams/list/
http://127.0.0.1:8000/teams/create
http://127.0.0.1:8000/teams/update/<int:pk>/
http://127.0.0.1:8000/teams/retrieve/<int:pk>/
http://127.0.0.1:8000/teams/destory/<int:pk>/
'''