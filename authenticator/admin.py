from authenticator.models import User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'email', 'business_manager_name',
                    'is_superuser', 'is_staff', '_brand_logo', 'change', 'history')
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_verified')
    search_fields = ('email', )
    ordering = ('email', )

    fieldsets = (
        (None, {
            'fields': ('owner_name', 'email', 'organization_name', 'business')
        }),
        ('Brand Logo™', {
            'classes': ('collapse',),
            'fields': ('brand_logo',)
        }),
        ('Timestamps⏳', {
            'classes': ('collapse',),
            'fields': ('date_joined', 'password_changes_datatime', 'login_datetime', 'logout_datetime', 'last_activity'),
            'description': 'Timestamps fields are automatically updated by the system.'
        }),
        ('Permissions🔐', {
            'classes': ('collapse',),
            'fields': (
                ('is_verified', 'is_superuser', 'is_active', ),
                ('is_staff', 'is_founder', 'is_ceo', 'is_manager',),
                ('is_employee', 'is_customer', 'is_supplier'),
                ('is_auditor', 'is_auditor_manager', 'is_auditor_head_office'),
                ('is_head_office', 'is_hr', 'is_accountant'),
            ),
            'description': 'Note: If you want to change the permissions of a user, you need to contact in our headquarters.'
        }),
        ('Session🛢', {
            'classes': ('collapse',),
            'fields': ('session',)
        }),
        ('Groups🏷', {
            'classes': ('collapse',),
            'fields': ('groups',)
        }),
    )

    def _brand_logo(self, obj):
        return format_html('<img src="{}" width="40" height="40"  loading=lazy /> '.format(obj.brand_logo))

    def change(self, obj):
        view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Change" />'.format(link)
        return format_html(html)

    def history(self, obj):
        view_name = "admin:{}_{}_history".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk])
        html = '<input type="button" onclick="location.href=\'{}\'" value="History" />'.format(link)
        return format_html(html)


# Note: Unregister the default admin group
admin.site.unregister(Group)
