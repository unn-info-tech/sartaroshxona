# Generated by Django 5.0 on 2024-01-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartaroshxona', '0002_remove_barber_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='organization_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
