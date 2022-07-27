from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from conference.forms import ParticipantForm, SpeakerForm, ConferenceForm
from conference.models import Conference, Speaker, Participant


def conferences(request):
    confs = Conference.objects.order_by('-created')
    return render(request,
                  'conference/conferences.html',
                  {'conferences': confs})


def conference_detail(request, id):
    # conf = Conference.objects.get(id=id)
    conf = get_object_or_404(Conference, id=id)
    return render(request,
                  'conference/conference_detail.html',
                  {'conference': conf})


def conference_registration(request, id):
    # form = SpeakerForm()
    conf = Conference.objects.get(id=id)
    form = ParticipantForm(initial={'conference': conf})
    if request.method == 'POST':
        form = ParticipantForm(request.POST, initial={'conference': conf})
        if form.is_valid():
            x = form.cleaned_data
    #         # Participant.objects.create(
    #         #     name=x['name'],
    #         #     conference=x['conference'],
    #         #     email=x['email'],
    #         #     phone=x['phone'],
    #         #     motivation=x['motivation']
    #         # )
            p = Participant(
                name=x['name'],
                conference=conf,
                email=x['email'],
                phone=x['phone'],
                motivation=x['motivation']
            )
            p.save()

    return render(request, 'conference/conf_register.html', {'form': form})


def yearly_conferences(request, year):
    return HttpResponse(year + "Conferences")


@login_required
def add_conf(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
            # messages.add_message(request, messages.ERROR, 'Invalid Data')
    else:
        form = ConferenceForm()
    return render(request, 'conference/add_conference.html', {'form': form})


@login_required()
def conference_edit(request, id):
    conf = get_object_or_404(Conference, id=id)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conf)
        if form.is_valid():
            form.save()
    else:
        form = ConferenceForm(instance=conf)
    return render(request, 'conference/edit_conference.html', {'form': form})