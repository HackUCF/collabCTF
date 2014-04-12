import json
from django.core.urlresolvers import resolve, Resolver404
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_safe, require_POST

from collabCTF.tools import crypto
from competition.forms import HashForm, RotForm
from competition.models import Competition


def home(request):
    return render_to_response('index.html')


def ctfoverview(request):
    return render_to_response('ctf/overview.html')


def ctfchallenge(request):
    return render_to_response('ctf/challenge/overview.html')


def reports(request):
    return render_to_response('reports.html')


def about(request):
    return render_to_response('about.html')


def addctfoverview(request):
    return render_to_response('ctf/add.html')


def profile(request):
    return render_to_response('profile.html')


def settings(request):
    return render_to_response('settings.html')


def sidebar(request):
    url = request.GET.get('url', None)
    if url is not None:
        try:
            resolved = resolve(url)
            view_name = resolved.view_name
        except Resolver404:
            view_name = 'index'
    else:
        view_name = 'index'
    data = {
        'ctfs': Competition.objects.prefetch_related('challenges'),
        'view_name': view_name
    }

    return render_to_response('sidebar.html', data)


@require_safe
def ctf_tools(request):
    data = {
        'hash_form': HashForm(),
        'rot_form': RotForm()
    }
    return render_to_response('ctftools.html', data, RequestContext(request))


@require_POST
def hash_val(request):
    form = HashForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': crypto.hash(cd['hash_type'], cd['value'])
        })
        return HttpResponse(jdata, content_type='application/json')

    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return HttpResponseBadRequest(jdata, content_type='application/json')


@require_POST
def rot_val(request):
    form = RotForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': crypto.rot(cd['rot_type'], cd['value'], cd['encode'])
        })
        return HttpResponse(jdata, content_type='application/json')
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return HttpResponseBadRequest(jdata, content_type='application/json')
