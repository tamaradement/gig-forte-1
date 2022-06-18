from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from .models import Gig


class DateTimePickerInput(forms.DateTimeInput):
    input_type = forms.DateTimeField(widget=AdminSplitDateTime)


class GigCreateForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ("title", "event_date", "bandleader", "location")

        def __init__(self, *args, **kwargs):
            super(GigCreateForm, self).__init__(*args, **kwargs)
            self.fields["event_date"].widget = DateTimePickerInput()
