from authenticator.models import User
from django.contrib import admin
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active', 'is_verified')
    list_filter = ('is_staff', 'is_active', 'is_verified')
    search_fields = ('email', )
    ordering = ('email',)


admin.site.unregister(Group)
