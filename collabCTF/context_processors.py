from django.core.urlresolvers import resolve

from competition.models import Competition


def ctf_sidebar(request):
    resolved = resolve(request.path)
    view_name = resolved.view_name
    context = {
        'sidebar': {
            'view_name': view_name,
            'ctfs': Competition.objects.all()
        }
    }

    return context