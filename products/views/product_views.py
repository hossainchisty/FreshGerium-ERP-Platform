from django.shortcuts import render
from django.views.generic import View


class ProductListView(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn list of products
        '''
        return render(request, 'products/product_list.html')


class CategoryListView(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn list of category
        '''
        return render(request, 'products/category_list.html')
