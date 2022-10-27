from rest_framework import serializers 
from .models import Tune

class TuneSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tune
        fields = (
            "id",
            "title",
            "composer",
            "key",
            "notes",
            "genre",
            "pdf",
            "performer",
        )
