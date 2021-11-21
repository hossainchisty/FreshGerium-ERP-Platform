from django.urls import include, path

urlpatterns = [
    path('api/', include('opportunities.api.urls.opportunities_urls')),
]
