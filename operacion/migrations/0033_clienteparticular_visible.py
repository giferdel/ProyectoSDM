# Generated by Django 4.2.17 on 2024-12-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0032_alter_automovil_vtv'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteparticular',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]