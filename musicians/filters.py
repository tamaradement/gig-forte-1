import django_filters
from accounts.models import CustomUser


class MusicianFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            "username": ["icontains"],
        }