from django import forms
from .models import Gig
from tunes.models import Setlist
from django.core.mail import send_mail
from tempus_dominus.widgets import DateTimePicker
from django.conf import settings


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
        widgets = {
            'event_date': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
        }    
    
    def __init__(self, performer, *args, **kwargs):
        super(GigCreateForm, self).__init__(*args, **kwargs)
        self.fields["setlist"].queryset = Setlist.objects.filter(performer=performer)
    
    def send_initial_gig_email(self):
        personnel = self.cleaned_data.get("personnel")
        bandleader_first_name = self.instance.bandleader.first_name
        bandleader_last_name = self.instance.bandleader.last_name
        from_email = settings.DEFAULT_FROM_EMAIL

        email_addresses = []
        for person in personnel:
            email_addresses.append(person.email)
            
        send_mail('New gig offer!', 'Hello! You have a new gig offer from {} {} on GigForte :) Sign in to your account! https://gig-forte-1.herokuapp.com/'.format(bandleader_first_name, bandleader_last_name), '{}'.format(from_email), email_addresses, fail_silently=False)
    
    def send_update_gig_email(self, gig):
        old_personnel = gig.personnel.all()
        personnel_store = {}

        for person in old_personnel:
            personnel_store[person] = True

        new_personnel = self.cleaned_data.get("personnel")
        email_addresses = []

        for person in new_personnel:
            if person not in personnel_store:
                email_addresses.append(person.email)

        bandleader_first_name = self.instance.bandleader.first_name
        bandleader_last_name = self.instance.bandleader.last_name
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail('New gig offer!', 'Hello! You have a new gig offer from {} {} on GigForte :) Sign in to your account! https://gig-forte-1.herokuapp.com/'.format(bandleader_first_name, bandleader_last_name), '{}'.format(from_email), email_addresses, fail_silently=False)
            
        

