import json
import sys

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from tools import crypto
from tools.forms import HashForm, RotForm, BaseConversionForm, XORForm, URLUnquoteForm, URLQuoteForm
from tools.misc import JSONResponse, JSONResponseBadRequest


if sys.version_info.major == 2:
    from urllib import quote as url_quote, unquote as url_unquote
elif sys.version_info.major == 3:
    # noinspection PyCompatibility
    # noinspection PyUnresolvedReferences
    from urllib.parse import quote as url_quote, unquote as url_unquote


@login_required
@require_POST
def hash_val(request):
    form = HashForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        value = cd['value']
        if sys.version_info.major == 3:
            value = value.encode('utf8')

        jdata = json.dumps({
            'result': crypto.hash_value(cd['hash_type'], value)
        })
        return JSONResponse(jdata)

    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)


@login_required
@require_POST
def rot_val(request):
    form = RotForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': crypto.rot(cd['rot_type'], cd['value'], cd['encode'])
        })
        return JSONResponse(jdata)
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)


@login_required
@require_POST
def base_conversion_val(request):
    form = BaseConversionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': crypto.base_conversions(cd['value'], cd['base'], cd['currBase'])
        })
        return JSONResponse(jdata)
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)


@login_required
@require_POST
def xor_val(request):
    form = XORForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': crypto.xor_tool(cd['value'], cd['key'])
        })
        return JSONResponse(jdata)
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)

@login_required
@require_POST
def quote_url(request):
    form = URLQuoteForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': url_quote(cd['value'])
        })
        return JSONResponse(jdata)
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)


@login_required
@require_POST
def unquote_url(request):
    form = URLUnquoteForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        jdata = json.dumps({
            'result': url_unquote(cd['value'])
        })
        return JSONResponse(jdata)
    else:
        jdata = json.dumps({
            'error': form.errors
        })
        return JSONResponseBadRequest(jdata)

