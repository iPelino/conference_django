from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def contact(request):
    return HttpResponse('Contact')
