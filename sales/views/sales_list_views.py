from django.shortcuts import render


def sales_list(request):
    '''
    TODO:
     - This will reutrn list of sales
    '''
    return render(request, 'sales/sales_list.html')
