"""
Track User Device Middleware.

"""
import json
import os
from urllib.request import urlopen

from django_user_agents.utils import get_user_agent
from dotenv import load_dotenv

from analytics.models import DeviceTrack
from django.utils import timezone

load_dotenv()  # take environment variables from .env.


class UserActivityMiddleware:
    '''
    Extract the user agent from the request and use it to determine the device type & as counted in the session variable.

    Extract the request user connected devices and os and device type.

        Example:
            Chrome Mobile 96, TECNO KE5, Android
            Chrome 98, Windows
            TECNO+KE5, Android App

    User location is determined using the device IP address.
        We fetch details about the people who request via the network.
        For example,
            IP address, city, country, region, organization.

    '''

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print('Initializing...')

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        user_agent = get_user_agent(request)

        # Accessing user agent's browser attributes

        request.user_agent.browser.family  # returns 'Mobile Safari'
        request.user_agent.browser.version_string   # returns '5.1'

        # Operating System properties
        request.user_agent.os  # returns 'iOS'
        request.user_agent.os.family  # returns 'iOS'

        # Device properties
        request.user_agent.device.family  # returns 'iPhone'

        url = os.getenv('IP_API_URL')
        response = urlopen(url)
        data = json.load(response)
        request.session['user_ip'] = data['ip']
        request.session['user_location'] = data['city']
        request.session['user_country'] = data['country']
        request.session['timezone'] = data['timezone']
        request.session['user_region'] = data['region']
        request.session['user_org'] = data['org']
        request.session.save()
        request.session.modified = True

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if 'admin' not in request.path or request.user.is_authenticated:
            last_seen = DeviceTrack.objects.filter(user__id=request.user.id).update(last_activity=timezone.now())
            if not last_seen:
                DeviceTrack.objects.update_or_create(
                    user=request.user,
                    user_agent=f'{request.user_agent.browser.family}, {request.user_agent.browser.version_string[0:2]}, {request.user_agent.os.family}',
                    ip_address=data['ip'],
                    location=data['city'],
                    timezone=data['timezone'],
                )
        return response
