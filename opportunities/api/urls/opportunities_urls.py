from django.urls import path
from opportunities.api.views import opportunities_views as views

urlpatterns = [
    path('list/', views.OpportunityAPIView.as_view()),
    path('create/', views.CreateOpportunity.as_view()),
    path('update/<int:pk>/', views.UpdateOpportunity.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveOpportunity.as_view()),
    path('destory/<int:pk>/', views.DestroyOpportunity.as_view())
]
