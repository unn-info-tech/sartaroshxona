# Generated by Django 5.0 on 2024-02-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartaroshxona', '0014_alter_barber_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='currency',
            field=models.CharField(choices=[('TJS', 'Tajik Somoni')], default='TJS', max_length=3),
        ),
    ]
