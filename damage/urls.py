from damage.views.add_manage_views import CreateDamage
from damage.views.damange_manage_views import DamageList
from damage.views.delete_damage_views import DeleteDamage
from damage.views.update_damage_views import UpdateDamage
from django.urls import path

urlpatterns = [
    path('', DamageList.as_view(), name='damage_list'),
    path('add/', CreateDamage.as_view(), name='add_damage'),
    path('update/<int:pk>/', UpdateDamage.as_view(), name='update_damage'),
    path('delete/<int:pk>/', DeleteDamage.as_view(), name='delete_damage'),
]
