# Generated by Django 5.0 on 2024-01-07 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_remove_appointment_service_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='total_duration',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='total_price',
        ),
    ]
