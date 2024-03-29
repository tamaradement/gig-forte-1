# Generated by Django 3.2.13 on 2022-10-02 22:02

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0020_auto_20220914_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='event_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 2, 0, 0, 0, 439965), help_text='Write date/time in this format: yyyy-mm-dd hh-mm-ss', null=True),
        ),
        migrations.AlterField(
            model_name='gig',
            name='personnel',
            field=models.ManyToManyField(blank=True, related_name='gig_staff', to=settings.AUTH_USER_MODEL),
        ),
    ]
