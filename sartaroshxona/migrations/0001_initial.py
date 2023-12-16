# Generated by Django 5.0 on 2023-12-14 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_work', models.TimeField()),
                ('end_work', models.TimeField()),
                ('launch_start_time', models.TimeField()),
                ('launch_end_time', models.TimeField()),
                ('location', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='working_time', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_minutes', models.PositiveIntegerField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='sartaroshxona.master')),
            ],
        ),
    ]
