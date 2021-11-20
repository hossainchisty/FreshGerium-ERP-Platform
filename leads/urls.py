from django.urls import include, path

urlpatterns = [
    path('api/', include('leads.api.urls.leads_urls')),
                            
]
