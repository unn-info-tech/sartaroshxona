# Generated by Django 5.0 on 2024-01-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='total_duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appointment',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
