# Generated by Django 3.2.13 on 2022-06-02 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('composer', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('genre', models.CharField(max_length=255)),
                ('pdf', models.FileField(blank=True, upload_to='pdfs')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
