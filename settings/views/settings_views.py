import pyshorteners
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from authenticator.models import User
from settings.forms.user_settings_form import UserSettingsForm


@login_required
def settings(request):
    user = get_object_or_404(User, pk=request.user.pk)
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

        # Check if brand_logo and defaultURL are not None before shortening
        brand_logo_short = None
        defaultURLshort = None
        if user.brand_logo:
            brand_logo_short = s.tinyurl.short(user.brand_logo.url)
        if user.defaultURL:
            defaultURLshort = s.tinyurl.short(user.defaultURL)

        context = {
            'form': UserSettingsForm(),
            'brand_logo_short': brand_logo_short,
            'defaultURLshort': defaultURLshort
        }
        return render(request, 'settings/settings.html', context)
