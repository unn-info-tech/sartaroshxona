# Generated by Django 5.0 on 2023-12-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartaroshxona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='currency',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('TJS', 'Tajik Somoni'), ('UZS', 'Uzbekistani Soʻm')], default='TJS', max_length=3),
        ),
    ]