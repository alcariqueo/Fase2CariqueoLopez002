# Generated by Django 3.1.2 on 2020-10-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0008_auto_20201024_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
