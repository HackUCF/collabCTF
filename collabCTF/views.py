from django.shortcuts import render_to_response


def home(request):
    return render_to_response('index.html')

def ctfoverview(request):
    return render_to_response('ctfoverview.html')

def ctfchallenge(request):
    return render_to_response('ctfchallenge.html')

def ctftools(request):
    return render_to_response('ctftools.html')

def reports(request):
    return render_to_response('reports.html')