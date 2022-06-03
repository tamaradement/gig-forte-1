# Generated by Django 3.2.13 on 2022-06-03 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tunes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tunes', models.ManyToManyField(to='tunes.Tune')),
            ],
        ),
    ]
