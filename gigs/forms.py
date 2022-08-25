from django import forms
from .models import Gig
from tunes.models import Setlist
from django.core.mail import send_mail


class GigCreateForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = (
            "title",
            "event_date",
            "location",
            "call_time",
            "start_time",
            "end_time",
            "pay",
            "setlist",
            "personnel",
        )
    
    def __init__(self, performer, *args, **kwargs):
        super(GigCreateForm, self).__init__(*args, **kwargs)
        self.fields["setlist"].queryset = Setlist.objects.filter(performer=performer)
    
    def send_email(self):
        personnel = self.cleaned_data.get("personnel")
        bandleader_first = self.instance.bandleader.first_name
        bandleader_last = self.instance.bandleader.last_name

        email_addresses = []
        for person in personnel:
            email_addresses.append(person.email)
            
        send_mail('New gig offer!', 'Hello! You have a new gig offer from {} {} on GigForte :) Sign in to your account! https://gig-forte-1.herokuapp.com/'.format(bandleader_first, bandleader_last), 'tamara.dement@gmail.com', email_addresses, fail_silently=False)

