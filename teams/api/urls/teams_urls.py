from django.urls import path
from teams.api.views import teams_views as views

urlpatterns = [
    path('list/', views.TeamAPIList.as_view()),
    path('create/', views.CreateTeam.as_view()),
    path('update/<int:pk>/', views.UpdateTeam.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveTeam.as_view()),
    path('destory/<int:pk>/', views.DestroyTeam.as_view())
]
