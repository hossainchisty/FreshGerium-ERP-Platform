from returns.models import Return
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View


class ReturnView(LoginRequiredMixin, View):
    def get(self, request):
        '''
        This will reutrn list of returns items
        '''
        return_list = Return.objects.all().order_by('-id')
        paginator = Paginator(return_list, 25)
        page_number = request.GET.get('page')
        returns = paginator.get_page(page_number)

        context = {
            'returns': returns
        }
        return render(request, 'return/manage_return.html', context)
