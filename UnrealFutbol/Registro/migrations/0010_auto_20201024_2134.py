# Generated by Django 3.1.2 on 2020-10-25 00:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0009_auto_20201024_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ff01ba2b-38fe-4c34-9435-78e3067d0066'), primary_key=True, serialize=False),
        ),
    ]
