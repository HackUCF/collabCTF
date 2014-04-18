import json
import datetime as dt

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Sum

from competition.models import Competition, Challenge


try:
    # not required since it's included, but...
    from pytz import UTC
except ImportError:
    from collabCTF.tools.misc import UTC


@login_required
@require_GET
def chart_data(request, ctf_slug):
    ctf = get_object_or_404(Competition.objects.prefetch_related('challenges'), slug=ctf_slug)
    challenges = ctf.challenges

    # compute aggregate data
    assert isinstance(ctf, Competition)
    solved_challenges = challenges.filter(progress=Challenge.SOLVED)
    in_progress_challenges = challenges.filter(progress=Challenge.IN_PROGRESS)
    challenges_data = {
        'total': challenges.count(),
        'in_progress': in_progress_challenges.count(),
        'solved': solved_challenges.count()
    }

    # Py2+3 unix time
    if ctf.start_time is not None:
        start_time = (ctf.start_time - dt.datetime(1970, 1, 1, tzinfo=UTC)).total_seconds()
    else:
        start_time = None
    if ctf.end_time is not None:
        end_time = (ctf.end_time - dt.datetime(1970, 1, 1, tzinfo=UTC)).total_seconds()
    else:
        end_time = None
    users = {
        'online': 4,
        'total': 22
    }

    pv_sum = Sum('point_value')
    points = {
        'earned': solved_challenges.aggregate(pv_sum)['point_value__sum'] or 0.001,
        'in_progress': in_progress_challenges.aggregate(pv_sum)['point_value__sum'] or 0.001,
        'total': challenges.aggregate(pv_sum)['point_value__sum'] or 1
    }

    data = {
        'challenges': challenges_data,
        'start_time': start_time,
        'end_time': end_time,
        'users': users,
        'points': points
    }

    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
@csrf_exempt
@require_POST
def track_challenge_visit(request):
    resolved = resolve(request.POST['url'])
    if resolved.view_name.endswith('challenge'):
        try:
            kwargs = resolved.kwargs
            challenge = Challenge.objects.get(competition__slug=kwargs['ctf_slug'], slug=kwargs['chall_slug'])
            if challenge.progress != Challenge.SOLVED:
                challenge.last_viewed = dt.datetime.now(UTC)
                challenge.save()
        except Challenge.DoesNotExist:
            pass
    return HttpResponse()