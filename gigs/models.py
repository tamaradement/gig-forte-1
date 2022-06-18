from django.conf import settings
from django.db import models
from django.urls import reverse


class Gig(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True)
    bandleader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gig_detail", args=[str(self.id)])


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    website = models.URLField(max_length=255, blank=True)
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venue_detail", args=[str(self.id)])
