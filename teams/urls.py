from django.urls import include, path

urlpatterns = [
   path('api/v1/', include('teams.api.urls.teams_urls')),
]
