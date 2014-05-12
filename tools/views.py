from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_safe

from tools.forms import HashForm, RotForm, BaseConversionForm, XorForm, URLUnquoteForm


@login_required
@require_safe
def ctf_tools(request):
    data = {
        'hash_form': HashForm(),
        'rot_form': RotForm(),
        'base_conversion_form': BaseConversionForm(),
        'xor_form': XorForm(),
        'unquote_form': URLUnquoteForm()
    }
    return render_to_response('tools.html', data, RequestContext(request))