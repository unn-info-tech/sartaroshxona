# Generated by Django 5.0 on 2024-01-15 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.city'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='coutry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.country'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.district'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.region'),
        ),
    ]
