from django.http import HttpResponse
from django.shortcuts import render
from conference.models import Conference, Speaker


def conferences(request):
    confs = Conference.objects.all()
    return render(request,
                  'conference/conferences.html',
                  {'conferences': confs})


def conference_detail(request, name):
    return HttpResponse(name + " Conference")


def conference_registration(request, name):
    return HttpResponse(name + " Conference Registration")


def yearly_conferences(request, year):
    return HttpResponse(year + "Conferences")