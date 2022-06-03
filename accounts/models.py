from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    instrument = models.CharField(blank=True, max_length=200)
