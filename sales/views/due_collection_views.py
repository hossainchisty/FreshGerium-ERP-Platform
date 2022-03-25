from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from sales.models import Sale


@method_decorator(cache_page(60 * 2), name='dispatch')
class DueCollection(View):
    ''' Due Collection '''

    def get(self, request):
        ''' Respond to a GET request '''
        due_list = Sale.objects.filter(status='due')
        due_amount = due_list.aggregate(Sum('due'))['due__sum']
        total_amount = Sale.objects.aggregate(Sum('total'))['total__sum']

        paginator = Paginator(due_list, 10)
        page_number = request.GET.get('page')

        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'due_list': page_object,
            'due_amount': due_amount,
            'total_amount': total_amount,
        }
        return render(request, 'sales/due_list.html', context)
