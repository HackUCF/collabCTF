from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.text import slugify
from django.views.decorators.http import require_safe, require_http_methods, require_POST

from competition.forms import CompetitionModelForm, ChallengeModelForm, ChallengeFileModelForm
from competition.models import Competition, Challenge, ChallengeFile


@require_http_methods(['GET', 'POST'])
def add_ctf(request):
    if request.method == 'GET':
        form = CompetitionModelForm()
        data = {
            'form': form
        }
        return render_to_response('ctf/add.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = CompetitionModelForm(request.POST)
        data = {
            '`form': form
        }

        if form.is_valid():
            competition = form.save(commit=False)
            competition.slug = slugify(competition.name)
            competition.save()
            data['competition'] = competition
            return redirect(competition.get_absolute_url())

        # url tbd
        return render_to_response('ctf/add.html', data, RequestContext(request))


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
        form = CompetitionModelForm(request.POST, instance=ctf)
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


@require_safe
def view_ctf(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=ctf_slug)
    challenges = ctf.challenges.all()
    data = {
        'ctf': ctf,
        'challenges': challenges
    }

    return render_to_response('ctf/overview.html', data, RequestContext(request))


@require_POST
def delete_ctf(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    data = {
        'ctf': ctf
    }
    response = render_to_response('ctf/removed.html', data)
    ctf.delete()
    return response


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
            challenge.competition = ctf
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
def update_challenge(request, ctf_slug, chall_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    challenge = get_object_or_404(Challenge.objects, competition=ctf, slug=chall_slug)
    if request.method == 'GET':
        data = {
            'challenge': challenge,
            'form': ChallengeModelForm(instance=challenge)
        }
        return render_to_response('ctf/challenge/update.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = ChallengeModelForm(request.POST, instance=challenge)
        saved = False
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.last_viewed = datetime.now()
            challenge.save()
            saved = True

        data = {
            'challenge': challenge,
            'form': ChallengeModelForm(instance=challenge),
            'saved': saved
        }
        return render_to_response('ctf/challenge/update.html', data, RequestContext(request))


@require_http_methods(['GET', 'POST'])
def delete_challenge(request, ctf_slug, chall_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    challenge = get_object_or_404(Challenge.objects, competition=ctf, slug=chall_slug)
    data = {
        'ctf': ctf,
        'challenge': challenge
    }
    response = render_to_response('ctf/challenge/deleted.html', data, RequestContext(request))
    challenge.delete()
    return response

@require_http_methods(['GET', 'POST'])
def add_file(request, ctf_slug, chall_slug):
    ctf = get_object_or_404(Competition.objects, slug=ctf_slug)
    challenge = get_object_or_404(Challenge.objects, competition=ctf, slug=chall_slug)

    data = {
        'ctf': ctf,
        'challenge': challenge,
    }

    if request.method == 'GET':
        data['form'] = ChallengeFileModelForm()
        return render_to_response('ctf/challenge/files/add.html', data, RequestContext(request))
    elif request.method == 'POST':
        form = ChallengeFileModelForm(request.POST, request.FILES)
        if form.is_valid():
            upfile = form.save(commit=False)
            upfile.challenge = challenge
            upfile.ctime = datetime.now()
            upfile.mtime = datetime.now()
            return redirect('view_challenge', ctf_slug=ctf_slug, chall_slug=chall_slug)
        else:
            data['form'] = ChallengeFileModelForm()
            return render_to_response('ctf/challenge/files/add.html', data, RequestContext(request))