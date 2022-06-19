from django import forms
from .models import Setlist, Tune


class SetlistForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ("title", "description", "tunes")

    def __init__(self, performer, *args, **kwargs):
        super(SetlistForm, self).__init__(*args, **kwargs)
        self.fields["tunes"].queryset = Tune.objects.filter(performer=performer)
