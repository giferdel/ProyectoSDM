# Generated by Django 4.2.17 on 2024-12-23 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0031_automovil_visibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovil',
            name='vtv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='operacion.vtvestado'),
        ),
    ]