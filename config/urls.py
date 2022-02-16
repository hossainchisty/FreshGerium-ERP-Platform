from django_otp.admin import OTPAdminSite

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from profiles.views.account_data_views import account_data

# admin.site.__class__ = OTPAdminSite

# Enforce 2FA only in production.
'''
if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite
'''
admin.site.site_header = 'Freshdesk CRM Platform'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('core.urls')),
    path('customers/', include('customers.urls')),
    path('profile/', include('profiles.urls')),
    path('purchase/', include('purchase.urls')),
    path('products/', include('products.urls')),
    path('service/', include('service.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('settings/', include('settings.urls')),
    path('sales/', include('sales.urls')),
    path('expense/', include('expense.urls')),
    path('return/', include('returns.urls')),
    path('damage/', include('damage.urls')),
    path('stock/', include('stock.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts-user/', include('allauth.urls')),
    path('auth/', include('authenticator.urls')),
    path('notifications/', include('notifications.urls')),
    path('accounts/access_tool/', account_data, name='account_data'),
    path('admin/defender/', include('defender.urls')),
]
