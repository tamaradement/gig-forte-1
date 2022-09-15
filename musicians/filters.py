import django_filters
from accounts.models import CustomUser
# from django.forms.widgets import TextInput

class MusicianFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            "username": ["icontains"],
        }
    #     widget={
    #         "username": TextInput(
    #             attrs={
    #                 'autofocus': True,
    #             }
    #         )
    #     }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(self.get_fields())

        # self.fields['username'].widget.attrs['autofocus'] = True