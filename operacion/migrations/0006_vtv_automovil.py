# Generated by Django 5.1.2 on 2024-10-13 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0005_vtv_alter_clienteempresa_cuit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vtv',
            name='automovil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='operacion.automovil'),
            preserve_default=False,
        ),
    ]
