from django.urls import path, include
urlpatterns = [
    path('api/', include('contacts.api.urls.contacts_urls')),
]
