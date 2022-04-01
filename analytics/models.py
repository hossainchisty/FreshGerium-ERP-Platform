from authenticator.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class DeviceTrack(models.Model):
    ''' Model for connected devices tracking '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), null=True, blank=True)
    user_agent = models.CharField(
        verbose_name='User Agent',
        help_text='e.g. Chrome 98, Windows, TECNO KE5, Android',
        max_length=255,
        blank=True, null=True,
    )
    last_activity = models.DateTimeField(
        verbose_name='Last Activity',
        help_text='Last activity of the device',
        null=True, blank=True,
    )
    ip_address = models.GenericIPAddressField(
        verbose_name='IP Address',
        help_text='IP address of the device',
        null=True, blank=True,
        default='',
    )

    location = models.CharField(
        verbose_name='Location',
        help_text='Location of the device',
        max_length=255,
        blank=True, null=True,
    )

    timezone = models.CharField(
        verbose_name='Timezone',
        max_length=255,
        blank=True, null=True,
    )

    class Meta:
        ''' Meta options for the model '''
        verbose_name = 'Device Activity'
        verbose_name_plural = 'Device Activity'
        ordering = ('-last_activity',)

    def __str__(self):
        ''' String representation of the model.'''
        return f'{self.user_agent} Last Activity - {self.last_activity}'


class Visitor(models.Model):
    '''
    Model for the visitor tracking devices.
    '''
    windows = models.IntegerField(default=0)
    mac = models.IntegerField(default=0)
    linux = models.IntegerField(default=0)
    android = models.IntegerField(default=0)
    ios = models.IntegerField(default=0)
    other = models.IntegerField(default=0)

    class Meta:
        ''' Meta options for the model '''
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    def __str__(self):
        ''' String representation of the model.'''
        return f'Windows: {self.windows}, Mac: {self.mac}, Linux: {self.linux}, Android: {self.android}, IOS: {self.ios}, Other: {self.other}'
