from django.shortcuts import render


def product_list(request):
    '''
    TODO:
     - This will reutrn list of products
    '''
    return render(request, 'products/product_list.html')
