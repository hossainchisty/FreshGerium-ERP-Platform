from accounts.api.views import accounts_views
from django.urls import path

urlpatterns = [
    path('list/', accounts_views.AccountAPIView.as_view()),
    path('create/', accounts_views.CreateAccount.as_view()),
    path('update/<int:pk>/', accounts_views.UpdateAccount.as_view()),
    path('retrieve/<int:pk>/', accounts_views.RetrieveAccount.as_view()),
    path('destory/<int:pk>/', accounts_views.DestroyAccount.as_view()),
]

'''
#? API endpoint of account
http://127.0.0.1:8000/accounts-user/list/
http://127.0.0.1:8000/accounts-user/create
http://127.0.0.1:8000/accounts-user/update/<int:pk>/
http://127.0.0.1:8000/accounts-user/retrieve/<int:pk>/
http://127.0.0.1:8000/accounts-user/destory/<int:pk>/
'''
