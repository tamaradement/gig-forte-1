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
            "setlist",
        )
