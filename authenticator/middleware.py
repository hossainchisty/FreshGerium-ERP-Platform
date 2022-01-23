"""
Fetch Request User Data Middleware.
This module provides a middleware that fetches user data from the request.
"""

import json
import os
from urllib.request import urlopen

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class FetchUserData:
    '''
    User location is determined using the device IP address.
    We fetch details about the people who request via the network.
    For example,
        IP address, city, country, region, organization.
    '''

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
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

        '''
        # Locations are approximate based on IP address.
        if request.session['user_country'] == 'BD':
            print('User is from Bangladesh.')
            print('User location:', request.session['user_location'])
            print('User IP:', request.session['user_ip'])
            print('User country:', request.session['user_country'])
            print('User timezone:', request.session['timezone'])
            print('User region:', request.session['user_region'])
            print('User org:', request.session['user_org'])
        '''

        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response
