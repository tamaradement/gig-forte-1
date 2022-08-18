from django import forms
from .models import Gig
from tunes.models import Setlist


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
