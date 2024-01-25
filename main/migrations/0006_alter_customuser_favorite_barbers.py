# Generated by Django 5.0 on 2024-01-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_customuser_phone_number'),
        ('sartaroshxona', '0003_barber_organization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favorite_barbers',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorited_by', to='sartaroshxona.barber'),
        ),
    ]
