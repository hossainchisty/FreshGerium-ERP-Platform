from django.urls import path
from opportunities.api.views import opportunities_views

urlpatterns = [
    path('list/', opportunities_views.OpportunityAPIView.as_view()),
    path('create/', opportunities_views.CreateOpportunity.as_view()),
    path('update/<int:pk>/', opportunities_views.UpdateOpportunity.as_view()),
    path('retrieve/<int:pk>/', opportunities_views.RetrieveOpportunity.as_view()),
    path('destory/<int:pk>/', opportunities_views.DestroyOpportunity.as_view())
]
