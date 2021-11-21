from contacts.api.views import contacts_views as views
from django.urls import path

urlpatterns = [
    path('list/', views.ContactList.as_view()),
    path('create/', views.CreateContact.as_view()),
    path('update/<int:pk>/', views.UpdateContact.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveContact.as_view()),
    path('destory/<int:pk>/', views.DestroyContact.as_view()),
]
