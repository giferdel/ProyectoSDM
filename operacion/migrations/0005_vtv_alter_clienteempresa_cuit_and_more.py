# Generated by Django 5.1.2 on 2024-10-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0004_clienteempresa_clienteparticular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vtv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vencimiento', models.CharField(max_length=50)),
                ('turno', models.BooleanField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='clienteempresa',
            name='cuit',
            field=models.PositiveBigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='clienteparticular',
            name='cuil',
            field=models.PositiveBigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='clienteparticular',
            name='dni',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
