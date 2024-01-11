# Generated by Django 5.0 on 2024-01-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_remove_appointment_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('in_queue', 'In Queue'), ('confirmed', 'Confirmed'), ('done', 'History')], default='in_queue', max_length=20),
        ),
    ]
