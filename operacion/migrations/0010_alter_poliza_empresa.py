# Generated by Django 5.1.2 on 2024-10-13 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0009_alter_vtv_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poliza',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='operacion.seguro'),
        ),
    ]