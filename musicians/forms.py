from django import forms

class NewMusicianForm(forms.Form):
    musician_first_name = forms.CharField(max_length=300)
    musician_email = forms.EmailField(max_length=300)

class GigsByYear(forms.Form):
    year = forms.IntegerField(help_text='Enter four digit year: yyyy')
    