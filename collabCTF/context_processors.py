from competition.models import Competition


def ctf_sidebar(request):
    context = {
        'sidebar': {
            'ctfs': Competition.objects.only('name', 'slug')
        }
    }

    return context