from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from service.models import Service
from utils.helper.decorators.filter import _currentUser


@method_decorator(cache_page(60 * 3), name='dispatch')
class ManageService(View):
    '''
    List of all services
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        service_list = Service.objects.all().order_by('-id')
        paginator = Paginator(service_list, 25)
        # Show 25 services per page.
        page_number = request.GET.get('page')
        services = paginator.get_page(page_number)

        context = {
            'services': services
        }
        return render(request, 'service/manage_service.html', context)
