# Generated by Django 2.2.1 on 2019-05-28 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20190528_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
