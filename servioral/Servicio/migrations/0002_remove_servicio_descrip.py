# Generated by Django 4.0.4 on 2022-05-19 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descrip',
        ),
    ]
