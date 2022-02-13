import pyshorteners

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from settings.forms.user_settings_form import UserSettingsForm


@login_required
@cache_page(60 * 15)
def settings(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email')
        owner_name = request.POST.get('owner_name')
        mobile_number = request.POST.get('mobile_number')
        organization_name = request.POST.get('organization_name')
        business = request.POST.get('business')
        business_manager_name = request.POST.get('business_manager_name')
        brand_logo = request.FILES.get('brand_logo_file')

        user.email = email
        user.owner_name = owner_name
        user.mobile_number = mobile_number
        user.organization_name = organization_name
        user.business = business
        user.business_manager_name = business_manager_name
        user.is_verified = True
        user.brand_logo = brand_logo
        user.save()
        messages.success(request, 'Your Settings has been updated. It may take a few moments to update across the site.')
        return redirect('settings')
    else:
        s = pyshorteners.Shortener()
        # short brand logo url
        brand_logo_short = s.tinyurl.short(request.user.brand_logo.url)

        context = {
            'form': UserSettingsForm(),
            'brand_logo_short': brand_logo_short,
        }
        return render(request, 'settings/settings.html', context)
