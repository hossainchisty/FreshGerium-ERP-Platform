from django.urls import path

from . views import( 
    AccountAPIView,
    CreateAccount,
    UpdateAccount,
    RetrieveAccount,
    DestroyAccount
)

urlpatterns = [
    path('list/', AccountAPIView.as_view()),
    path('create/', CreateAccount.as_view()),
    path('update/<int:pk>/', UpdateAccount.as_view()),
    path('retrieve/<int:pk>/', RetrieveAccount.as_view()), 
    path('destory/<int:pk>/', DestroyAccount.as_view()),
]

'''
#? API endpoint of account
http://127.0.0.1:8000/accounts-user/list/
http://127.0.0.1:8000/accounts-user/create
http://127.0.0.1:8000/accounts-user/update/<int:pk>/
http://127.0.0.1:8000/accounts-user/retrieve/<int:pk>/
http://127.0.0.1:8000/accounts-user/destory/<int:pk>/
'''