# Generated by Django 5.0 on 2024-01-07 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_address_ru_moscow_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
