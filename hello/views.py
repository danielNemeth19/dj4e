from django.conf import settings
from django.http import HttpResponse


def session_counter(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del (request.session['num_visits'])
    response = HttpResponse('view count=' + str(num_visits))
    response.set_cookie('dj4e_cookie', settings.OWNER_HASH, max_age=1000)
    return response
