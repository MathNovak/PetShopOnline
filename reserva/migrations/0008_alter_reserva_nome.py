# Generated by Django 4.1.6 on 2023-02-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0007_reserva_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
