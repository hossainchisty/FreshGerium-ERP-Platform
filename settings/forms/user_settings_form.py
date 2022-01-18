from authenticator.models import User
from django.forms import ModelForm


class UserSettingsForm(ModelForm):
    ''' Form asking for update user Information '''
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['first_name', 'last_name', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions', 'otp', 'otp_created_time', 'token', 'is_verified', 'session', 'ip_address', 'is_founder',
                   'is_ceo', 'is_admin', 'is_manager', 'is_head_office', 'is_hr', 'is_accountant', 'is_auditor', 'is_auditor_manager', 'is_auditor_head_office', 'is_employee', 'is_customer', 'is_supplier', 'created_at', 'brand_logo']
