# Generated by Django 3.2.13 on 2022-06-19 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunes', '0002_setlist'),
        ('gigs', '0006_gig_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='call_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gig',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 6, 19, 9, 57, 52, 683353)),
        ),
        migrations.AddField(
            model_name='gig',
            name='pay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gig',
            name='setlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tunes.setlist'),
        ),
        migrations.AddField(
            model_name='gig',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2022, 6, 19, 9, 57, 52, 683333)),
        ),
    ]
