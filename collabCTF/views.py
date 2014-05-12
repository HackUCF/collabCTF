import json
import sys

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.conf import settings

from competition.forms import RegistrationForm, LoginForm, \
    PasswordChangeForm, EmailChangeForm
from competition.models import Competition, Challenge


@login_required
def index(request):
    recently_viewed = Challenge.objects.order_by('-last_viewed')
    recently_solved = Challenge.objects.filter(progress=Challenge.SOLVED)
    data = {
        'recently_solved': recently_solved[:5],
        'recently_viewed': recently_viewed[:5]
    }
    return render_to_response('index.html', data, RequestContext(request))


@login_required
def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))


@login_required
def user_settings(request):
    if request.method == 'GET':
        data = {
            'password_form': PasswordChangeForm(request.user),
            'email_form': EmailChangeForm()
        }

        return render_to_response('settings.html', data, context_instance=RequestContext(request))
    else:
        password_changed = False
        password_form = PasswordChangeForm(request.user, data=request.POST)
        if password_form.is_valid():
            cd = password_form.cleaned_data
            password_form.save()
            password_changed = True
            password_form = PasswordChangeForm(request.user)

        data = {
            'password_form': password_form,
            'password_changed': password_changed
        }
        return render_to_response('settings.html', data, context_instance=RequestContext(request))


@login_required
def ctfoverview(request):
    return render_to_response('ctf/overview.html')


@login_required
def ctfchallenge(request):
    return render_to_response('ctf/challenge/overview.html')


@login_required
@require_safe
def reports(request):
    data = {
        'ctfs': Competition.objects.order_by('-start_time')
    }
    return render_to_response('reports.html', data, RequestContext(request))


def register(request):
    if request.user.is_authenticated():
        return redirect('index')

    elif settings.REGISTRATION_LOCK:
        resp = render_to_response('registration_locked.html', {}, RequestContext(request))
        resp.status_code = 403
        return resp

    if request.method == 'GET':
        form = RegistrationForm()
        data = {
            'register_form': form
        }
        return render_to_response('register.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        data = {
            'register_form': form
        }

        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            data['user'] = user
            return redirect(reverse('login'))

        return render_to_response('register.html', data, RequestContext(request))


@require_http_methods(['GET', 'POST'])
def log_in(request):
    if request.method == 'GET':
        data = {
            'login_form': LoginForm()
        }

        return render_to_response('login.html', data, RequestContext(request))

    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index'))

        data = {
            'login_form': form
        }
        return render_to_response('login.html', data, RequestContext(request))

