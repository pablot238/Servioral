# Generated by Django 4.0.4 on 2022-05-10 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Odontologo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False, verbose_name='Id acudiente')),
                ('date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('id_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Odontologo.odontologo')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
            },
        ),
    ]