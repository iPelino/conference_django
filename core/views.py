from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request, 'core/contact.html')


def manage(request):
    return render(request, 'core/manage.html')