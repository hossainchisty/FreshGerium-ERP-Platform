from damage.forms.damage_form import DamageForm
from django.shortcuts import redirect, render
from django.views import View


class CreateDamage(View):
    ''' Create a new purchase '''

    def get(self, request, *args, **kwargs):
        ''' Respond to GET request '''
        return render(request,  'damage/add_damage.html', {'forms': DamageForm()})

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        form = DamageForm(request.POST)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            ''' Provide a redirect on GET request. '''
            return redirect('damage_list')
        else:
            return render(request, 'damage/add_damage.html', {'forms': form})
