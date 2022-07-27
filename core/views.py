from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from conference.models import Conference


def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request, 'core/contact.html')


@login_required(login_url='home')
def manage(request):
    confs = Conference.objects.all()
    return render(request, 'core/manage.html', {'confs': confs})