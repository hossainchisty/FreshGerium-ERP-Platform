from django.shortcuts import render


def suppliers_list(request):
    '''
    TODO:
     - This will reutrn list of suppliers
    '''
    return render(request, 'suppliers/suppliers_list.html')
