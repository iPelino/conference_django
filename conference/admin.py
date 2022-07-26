from django.contrib import admin
from conference.models import Speaker, Conference, Schedule, Participant

admin.site.register(Speaker)
admin.site.register(Conference)
admin.site.register(Schedule)
admin.site.register(Participant)
