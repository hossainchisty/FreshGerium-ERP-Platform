from damage.models import Damage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser


class DamageList(LoginRequiredMixin, View):

    @method_decorator(_currentUser())
    def get(self, request):
        '''
        This will reutrn list of damage items
        '''
        damage_list = Damage.objects.all().order_by('-id')
        paginator = Paginator(damage_list, 25)
        page_number = request.GET.get('page')
        damage = paginator.get_page(page_number)

        context = {
            'damages': damage
        }
        return render(request, 'damage/manage_damage.html', context)
