from contacts.views.contact_views import contact
from django.urls import include, path

urlpatterns = [
    path('', contact, name='contact'),
    path('api/v1/', include('contacts.api.urls.contacts_urls')),
]
