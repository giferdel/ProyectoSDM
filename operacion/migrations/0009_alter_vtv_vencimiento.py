# Generated by Django 5.1.2 on 2024-10-13 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0008_remove_coberturas_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vtv',
            name='vencimiento',
            field=models.DateField(),
        ),
    ]
