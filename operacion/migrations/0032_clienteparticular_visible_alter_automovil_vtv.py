# Generated by Django 5.1.3 on 2024-12-24 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0031_automovil_visibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteparticular',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='vtv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='operacion.vtvestado'),
        ),
    ]