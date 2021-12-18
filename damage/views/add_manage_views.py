from damage.forms.damage_form import DamageForm
from django.shortcuts import redirect, render
from django.views import View


class CreateDamage(View):
    '''
    Intentionally simple parent class for all views.
    '''
    def get(self, request, *args, **kwargs):
        return render(request,  'damage/add_damage.html', {'forms': DamageForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new purchase '''
        form = DamageForm(request.POST)
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('damage_list')
        else:
            return render(request, 'damage/add_damage.html', {'forms': form})
