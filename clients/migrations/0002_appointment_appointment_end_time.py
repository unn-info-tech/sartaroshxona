# Generated by Django 5.0 on 2024-01-18 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 19, 4, 12, 480495, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]