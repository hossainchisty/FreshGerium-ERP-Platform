from django.urls import path
from products.views.add_category_views import CreateCategory
from products.views.add_unit_views import CreateUnit
from products.views.product_views import CategoryListView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catetory/list', CategoryListView.as_view(), name='category_list'),
    path('add/catetory', CreateCategory.as_view(), name='create_category'),
    path('add/unit', CreateUnit.as_view(), name='create_unit'),
]
