from mq.models import *
from django.http import HttpResponseRedirect, HttpResponse, Http404

def richieste(request):
    return HttpResponse('ciao')
    """
    return render_to_response(
        'homepage.html', {
            'login_form': LoginForm(),
            'signup_form': KcSignupForm(),
        },
        context_instance=RequestContext(request)
    )
    """
