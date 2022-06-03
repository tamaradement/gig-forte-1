import django_filters
from .models import Tune


class TuneFilter(django_filters.FilterSet):
    class Meta:
        model = Tune
        fields = {
            "title": ["icontains"],
            "composer": ["icontains"],
            "genre": ["icontains"],
        }
