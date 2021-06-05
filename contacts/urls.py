from django.urls import path

from . views import( 
    ContactList,
    CreateContact,
    UpdateContact,
    RetrieveContact,
    DestroyContact
)

urlpatterns = [
    path('list/', ContactList.as_view()),
    path('create/', CreateContact.as_view()),

    path('update/<int:pk>/', UpdateContact.as_view()),
    
    path('retrieve/<int:pk>/', RetrieveContact.as_view()), 
    path('destory/<int:pk>/', DestroyContact.as_view()),
]

'''
#? API endpoint of contacts
http://127.0.0.1:8000/contacts/list/
http://127.0.0.1:8000/contacts/create
http://127.0.0.1:8000/contacts/update/<int:pk>/
http://127.0.0.1:8000/contacts/retrieve/<int:pk>/
http://127.0.0.1:8000/contacts/destory/<int:pk>/
'''