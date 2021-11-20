from contacts.api.views import contacts_views
from django.urls import path

urlpatterns = [
    path('list/', contacts_views.ContactList.as_view()),
    path('create/', contacts_views.CreateContact.as_view()),
    path('update/<int:pk>/', contacts_views.UpdateContact.as_view()),
    path('retrieve/<int:pk>/', contacts_views.RetrieveContact.as_view()),
    path('destory/<int:pk>/', contacts_views.DestroyContact.as_view()),
]
