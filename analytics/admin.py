from analytics.models import DeviceTrack, Visitor
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.html import format_html


@admin.register(DeviceTrack)
class DeviceTrackAdmin(admin.ModelAdmin):
    ''' Admin for DeviceTrack model '''
    list_display = ('user_agent', 'location', 'timezone', '_last_activity', 'ip_address')
    list_filter = ('user_agent', 'last_activity')
    search_fields = ('user_agent', 'last_activity', 'ip_address')

    def _last_activity(self, obj):
        ''' Last seen time '''
        return format_html('<span style="color: #008000; font-weight: bold;">{}</span>', naturaltime(obj.last_activity))

    # def get_queryset(self, request):
    #     ''' Override the default queryset to return only the latest 100 records '''
    #     return super().get_queryset(request).order_by('-last_activity')[:100]


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    ''' Admin for Visitor model '''
    list_display = ('windows', 'mac', 'linux', 'android', 'ios', 'other')
    list_filter = ('windows', 'mac', 'linux', 'android', 'ios', 'other')
    search_fields = ('windows', 'mac', 'linux', 'android', 'ios', 'other')
