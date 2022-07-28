from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from tunes.models import Setlist
from accounts.models import CustomUser


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


class Gig(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True)
    bandleader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(Venue, on_delete=models.PROTECT, blank=True, null=True)
    call_time = models.TimeField(blank=True, null=True)
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField(default=datetime.now())
    pay = models.IntegerField(default=0)
    setlist = models.ForeignKey(
        Setlist, on_delete=models.PROTECT, blank=True, null=True
    )
    personnel = models.ManyToManyField(CustomUser, related_name='gig_staff')
    acccepts = models.ManyToManyField(CustomUser, related_name='gig_accepts')
    declines = models.ManyToManyField(CustomUser, related_name='gig_declines')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gig_detail", args=[str(self.id)])
