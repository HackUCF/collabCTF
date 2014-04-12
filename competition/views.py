from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_safe
from competition.forms import ChallengeModelForm

from competition.models import Competition, Challenge


@require_safe
def view_ctf(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=ctf_slug)
    challenges = ctf.challenges.all()
    data = {
        'ctf': ctf,
        'challenges': challenges
    }

    return render_to_response('ctf/overview.html', data)


def add_challenge(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    if request.method == 'GET':
        form = ChallengeModelForm()
        data = {
            'form': form,
            'ctf': ctf
        }
        return render_to_response('ctf/challenge/add.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = ChallengeModelForm(request.POST)
        data = {
            'form': form,
            'ctf': ctf
        }

        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.competition = ctf
            challenge.last_viewed = datetime.now()
            challenge.save()
            data['challenge'] = challenge

        return render_to_response('ctf/challenge/add.html', data, RequestContext(request))


def view_challenge(request, ctf_slug, chall_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    challenge = get_object_or_404(Challenge.objects, competition=ctf, slug=chall_slug)

    data = {
        'ctf': ctf,
        'challenge': challenge
    }

    return render_to_response('ctf/challenge/overview.html', data, RequestContext(request))