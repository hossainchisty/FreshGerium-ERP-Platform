"""
Track User Device Middleware.
This module provides a middleware that implements the tracking of user devices.
"""
import threading

from django_user_agents.utils import get_user_agent


class TrackUserDevice:
    '''
    Extract the user agent from the request and use it to determine the device type & as counted in the session variable.
    '''

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        user_agent = get_user_agent(request)

        # # Device properties
        # request.user_agent.device  # returns Device(family='iPhone')
        # request.user_agent.device.family  # returns 'iPhone'
        # Accessing user agent's browser attributes
    # request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    # request.user_agent.browser.family  # returns 'Mobile Safari'
    # request.user_agent.browser.version  # returns (5, 1)
    # request.user_agent.browser.version_string   # returns '5.1'

        mobile_visit = request.session.get('mobile_visit', 0)
        pc_visit = request.session.get('pc_visit', 0)
        tablet_visit = request.session.get('tablet_visit', 0)

        if user_agent.is_mobile:
            # Get a session value by its key (e.g. 'mobile_visit'), raising a KeyError if the key is not present
            request.session['mobile_visit'] = mobile_visit + 1
            request.session.save()
        if user_agent.is_pc:
            request.session['pc_visit'] = pc_visit + 1
            request.session.save()
        if user_agent.is_tablet:
            request.session['tablet_visit'] = tablet_visit + 1
            request.session.save()
        # Set session as modified to force data updates/cookie to be saved.
        request.session.modified = True

        # total_visitor = pc_visit + mobile_visit + tablet_visit
        # print(f'PC: {pc_visit}')
        # print(f'Mobile: {mobile_visit}')
        # print(f'Tablet: {tablet_visit}')
        # print(f'Total: {total_visitor}')

        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response


class RequestMiddleware:
    '''
    Access Request Object Inside the Models and Signals.
    Note: I don't know is it good practice to access request object inside the models and signals.
    '''

    def __init__(self, get_response, thread_local=threading.local()):
        self.get_response = get_response
        self.thread_local = thread_local
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.thread_local.current_request = request

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
