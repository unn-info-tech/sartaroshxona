# Generated by Django 5.0 on 2024-01-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartaroshxona', '0007_alter_barber_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='barber',
            name='payment_expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]