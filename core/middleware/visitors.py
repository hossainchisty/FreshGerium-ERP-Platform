from django_user_agents.utils import get_user_agent

from django.db.models import F


class UserStatisticsMiddleware:
    '''
    "UserStatistics" middleware for counting the user device type (e.g. Mobile, Tab, PC)  and save it in the session variable.

    '''

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Imported user_agent library to extract the user device details.
        user_agent = get_user_agent(request)

        mobile_visit = request.session.get('mobile_visit', 0)
        pc_visit = request.session.get('pc_visit', 0)
        tablet_visit = request.session.get('tablet_visit', 0)

        '''
        Get a session value by its key (e.g. 'mobile_visit').

        :raises: if the key is not present in sesstion raising a KeyError.
        :return: the value associated with the key. if the key does not exist, it will return 0.

        '''
        from analytics.models import Visitor
        if user_agent.is_mobile:
            request.session['mobile_visit'] = mobile_visit + 1
            request.session.save()
            Visitor.objects.all().update(android=F('android') + 1)
        if user_agent.is_pc:
            request.session['pc_visit'] = pc_visit + 1
            request.session.save()
            Visitor.objects.update_or_create(
                windows=+1
            )

        if user_agent.is_tablet:
            request.session['tablet_visit'] = tablet_visit + 1
            request.session.save()
        # Set session as modified to force data updates/cookie to be saved.
        request.session.modified = True

        total_visitor = pc_visit + mobile_visit + tablet_visit
        print(f'PC: {pc_visit}')
        print(f'Mobile: {mobile_visit}')
        print(f'Tablet: {tablet_visit}')
        print(f'Total: {total_visitor}')

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response
