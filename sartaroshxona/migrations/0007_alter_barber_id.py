# Generated by Django 5.0 on 2024-01-30 08:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sartaroshxona', '0006_alter_barber_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
