# Generated by Django 5.0 on 2024-01-06 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sartaroshxona', '0002_alter_barber_location_alter_barber_phone_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.DateTimeField()),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barber_appointments', to='sartaroshxona.barber')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_appointments', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_appointments', to='sartaroshxona.service')),
            ],
        ),
    ]
