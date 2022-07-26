from django import forms

from conference.models import Conference, Speaker


class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=200)
    # conference = forms.ModelChoiceField(queryset=Conference.objects.all())
    conference = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone  = forms.CharField()
    motivation = forms.CharField(max_length=1000, widget=forms.Textarea)


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = '__all__'
        exclude = ['profile_picture']


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'start_date', 'end_date', 'venue', 'entry_fee', 'speakers']
