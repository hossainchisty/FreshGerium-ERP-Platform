from accounts.api.views import accounts_views as views
from django.urls import path

urlpatterns = [
    path('list/', views.AccountAPIView.as_view()),
    path('create/', views.CreateAccount.as_view()),
    path('update/<int:pk>/', views.UpdateAccount.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveAccount.as_view()),
    path('destory/<int:pk>/', views.DestroyAccount.as_view()),
]
