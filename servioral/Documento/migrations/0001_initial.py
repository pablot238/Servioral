# Generated by Django 4.0.4 on 2022-05-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocu', models.CharField(choices=[(1, 'Registro civil'), (2, 'Tarjeta de identidad'), (3, 'Cédula de ciudadania'), (4, 'Cédula de extrangeria'), (5, 'Pasaporte')], max_length=200, verbose_name='Tipo de documento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
