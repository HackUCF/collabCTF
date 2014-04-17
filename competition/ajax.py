import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from competition.models import Competition, Challenge
from django.db.models import Sum

import datetime as dt

try:
    # not required since it's included, but...
    from pytz import UTC
except ImportError:
    from collabCTF.tools.misc import UTC


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
    start_time = (ctf.start_time - dt.datetime(1970, 1, 1, tzinfo=UTC)).total_seconds()
    end_time = (ctf.end_time - dt.datetime(1970, 1, 1, tzinfo=UTC)).total_seconds()
    users = {
        'online': 4,
        'total': 22
    }

    pv_sum = Sum('point_value')
    points = {
        'earned': solved_challenges.aggregate(pv_sum)['point_value__sum'] or 0,
        'in_progress': in_progress_challenges.aggregate(pv_sum)['point_value__sum'] or 0,
        'total': challenges.aggregate(pv_sum)['point_value__sum'] or 0
    }

    data = {
        'challenges': challenges_data,
        'start_time': start_time,
        'end_time': end_time,
        'users': users,
        'points': points
    }

    return HttpResponse(json.dumps(data), content_type='application/json')