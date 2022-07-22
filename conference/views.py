from django.http import HttpResponse
from django.shortcuts import render


def conferences(request, year=None):
    return HttpResponse('All Conferences')


def conference_detail(request, name):
    return HttpResponse(name + " Conference")


def conference_registration(request, name):
    return HttpResponse(name + " Conference Registration")


def yearly_conferences(request, year):
    return HttpResponse(year + "Conferences")