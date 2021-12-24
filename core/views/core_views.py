from django_user_agents.utils import get_user_agent

from django.shortcuts import render
from django.views.generic import View


class Dashboard(View):
    def get(self, request):
        ''''
        Main dashboard view for the application.

        Extract the user agent from the request and use it to determine the device type & as counted in the session variable.
        '''
        user_agent = get_user_agent(request)
        movile_visit = request.session.get('movile_visit', 0)
        pc_visit = request.session.get('pc_visit', 0)
        tablet_visit = request.session.get('tablet_visit', 0)
        num_visits = request.session.get('num_visits', 0)

        if user_agent.is_mobile:
            request.session['movile_visit'] = movile_visit + 1
        elif user_agent.is_pc:
            request.session['pc_visit'] = pc_visit + 1
        elif user_agent.is_tablet:
            request.session['tablet_visit'] = tablet_visit + 1
        else:
            request.session['num_visits'] = num_visits + 1

        return render(request, 'core/dashboard.html', {
            'mobile_device': movile_visit,
            'desktop_device': pc_visit,
            'tablet_device': tablet_visit}
            )
