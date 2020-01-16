from user_agents import parse
from django.http.response import Http404
from django.middleware.common import CommonMiddleware


def check_user_agent(get_response):

    def middleware(request):

        ua_string = request.META.get('HTTP_USER_AGENT')
        # 'ChatBot_App/1 CFNetwork/808.3 Darwin/16.3.0'
        user_agent = parse(ua_string)
        print(user_agent.browser.family)

        if user_agent.browser.family != 'ChatBot_App':
            raise Http404

        response = get_response(request)

        return response

    return middleware


def is_registered_user(get_response):

    def middleware(request):

        response = get_response(request)

        return response

    return middleware
