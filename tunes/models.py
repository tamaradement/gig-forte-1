from django.conf import settings
from django.db import models
from django.urls import reverse


class Tune(models.Model):
    title = models.CharField(max_length=255)
    composer = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    notes = models.TextField()
    genre = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdfs", blank=True)
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tune_detail", args=[str(self.id)])


class Setlist(models.Model):
    title = models.CharField(max_length=255)
    performer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=255)
    tunes = models.ManyToManyField(Tune)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("setlist_detail", args=[str(self.id)])
