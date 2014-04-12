from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_safe, require_POST

from collabCTF.tools import crypto
from competition.forms import HashForm


def home(request):
    return render_to_response('index.html')


def ctfoverview(request):
    return render_to_response('ctfoverview.html')


def ctfchallenge(request):
    return render_to_response('ctfchallenge.html')


def reports(request):
    return render_to_response('reports.html')


@require_safe
def ctf_tools(request):
    data = {
        'hash_form': HashForm()
    }
    print data
    return render_to_response('ctftools.html', data, RequestContext(request))


@require_POST
def hash_val(request):
    form = HashForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = {
            'result': crypto.hash(cd['hash_type'], cd['value'])
        }
        return HttpResponse(jdata, content_type='application/json')
    else:
        jdata = {
            'error': form.errors
        }
        return HttpResponseBadRequest(jdata, content_type='application/json')
