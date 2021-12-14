from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from products.models import Category, Product


class ProductListView(View):
    def get(self, request):
        ''' This will reutrn list of products '''
        product_list = Product.objects.all().order_by('-id')

        paginator = Paginator(product_list, 25) # Show 25 customers per page.
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        context = {
            'products': products,
        }
        return render(request, 'products/product_list.html', context)


class CategoryListView(View):
    def get(self, request):
        ''' This will reutrn list of category '''
        category_list = Category.objects.all().order_by('-id')
        paginator = Paginator(category_list, 25) # Show 25 customers per page.
        page_number = request.GET.get('page')
        category = paginator.get_page(page_number)

        context = {
            'category': category,
        }
        return render(request, 'products/category_list.html', context)
