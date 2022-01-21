from django.contrib import messages
from django.shortcuts import redirect, render
from settings.forms.user_settings_form import UserSettingsForm


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
        messages.success(request, 'Settings updated successfully')
        return redirect('settings')
    else:
        return render(request, 'settings/settings.html', {'form': UserSettingsForm()})
