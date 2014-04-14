from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.text import slugify
from django.views.decorators.http import require_safe, require_http_methods

from competition.forms import CompetitionModelForm, ChallengeModelForm
from competition.models import Competition, Challenge


@require_http_methods(['GET', 'POST'])
def add_ctf(request):
    if request.method == 'GET':
        form = CompetitionModelForm()
        data = {
            'form': form
        }
        return render_to_response('ctf/add.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = CompetitionModelForm(request.POST, fieldset_title='Update competition')
        data = {
            'form': form
        }

        if form.is_valid():
            competition = form.save(commit=False)
            competition.slug = slugify(competition.name)
            competition.save()
            data['competition'] = competition
        # url tbd
        return render_to_response('ctf/add.html', data, RequestContext(request))


@require_safe
def view_ctf(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=ctf_slug)
    challenges = ctf.challenges.all()
    data = {
        'ctf': ctf,
        'challenges': challenges
    }

    return render_to_response('ctf/overview.html', data)


@require_http_methods(['GET', 'POST'])
def add_challenge(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    if request.method == 'GET':
        form = ChallengeModelForm(initial={'competition': ctf})
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
            challenge.last_viewed = datetime.now()
            challenge.slug = slugify(challenge.name)
            challenge.save()
            data['challenge'] = challenge
            data['form'] = ChallengeModelForm()

        return render_to_response('ctf/challenge/add.html', data, RequestContext(request))


@require_safe
def view_challenge(request, ctf_slug, chall_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    challenge = get_object_or_404(Challenge.objects, competition=ctf, slug=chall_slug)

    data = {
        'ctf': ctf,
        'challenge': challenge
    }

    return render_to_response('ctf/challenge/overview.html', data, RequestContext(request))


@require_http_methods(['GET', 'POST'])
def update_ctf(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    if request.method == 'GET':
        data = {
            'ctf': ctf,
            'form': CompetitionModelForm(instance=ctf)
        }
        return render_to_response('ctf/update.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = CompetitionModelForm(request.POST)
        saved = False
        if form.is_valid():
            form.save()
            saved = True

        data = {
            'ctf': ctf,
            'form': form,
            'saved': saved
        }
        return render_to_response('ctf/update.html', data, RequestContext(request))