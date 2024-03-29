# Generated by Django 3.2.13 on 2022-07-28 13:38

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0009_auto_20220724_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='declines',
            field=models.ManyToManyField(related_name='gig_declines', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gig',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 28, 9, 38, 13, 912184)),
        ),
        migrations.AlterField(
            model_name='gig',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2022, 7, 28, 9, 38, 13, 912160)),
        ),
    ]
