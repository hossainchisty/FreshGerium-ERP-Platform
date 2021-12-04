from django.urls import path
from products.views.product_views import ProductListView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catetory/list', CategoryListView.as_view(), name='category_list'),
]
