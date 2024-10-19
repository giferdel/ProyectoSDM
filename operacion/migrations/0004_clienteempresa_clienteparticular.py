# Generated by Django 5.1.2 on 2024-10-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0003_seguro_alter_automovil_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cuit', models.PositiveBigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteParticular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.PositiveBigIntegerField()),
                ('cuil', models.PositiveBigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]