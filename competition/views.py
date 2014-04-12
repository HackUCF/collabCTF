from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.http import require_safe, require_POST

from competition.models import Competition
from competition.forms import HashForm
import competition.tools.crypto as crypto


@require_safe
def view_ctf(request, ctf_slug):
    competition = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=ctf_slug)
    challenges = competition.challenges.all()
    data = {
        'ctf': competition,
        'challenges': challenges
    }

    return render_to_response('ctfoverview.html', data)