from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('opportunities.api.urls.opportunities_urls')),
]
