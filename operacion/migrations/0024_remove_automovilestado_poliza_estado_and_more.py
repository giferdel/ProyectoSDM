# Generated by Django 5.1.2 on 2024-10-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0023_rename_poliza_automovilestado_poliza_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automovilestado',
            name='poliza_estado',
        ),
        migrations.RemoveField(
            model_name='automovilestado',
            name='vtv_estado',
        ),
    ]
