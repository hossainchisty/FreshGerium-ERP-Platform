from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from returns.models import Return


class WastageReturnView(View):
    def get(self, request):
        '''
        This will reutrn list of wastage items
        '''
        wastage_list = Return.objects.all()
        paginator = Paginator(wastage_list, 10)
        page_number = request.GET.get('page')
        wastage = paginator.get_page(page_number)

        context = {
            'wastage_return': wastage,
        }
        return render(request, 'return/wastage_return.html', context)
