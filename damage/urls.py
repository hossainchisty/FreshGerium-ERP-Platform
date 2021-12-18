from damage.views.damange_manage_views import DamageList
from django.urls import path

urlpatterns = [
    path('', DamageList.as_view(), name='damage_list'),
]
