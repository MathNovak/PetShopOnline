# Generated by Django 4.1.6 on 2023-02-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_remove_reserva_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='tamanho',
            field=models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')], null=True, verbose_name='Tamanho'),
        ),
    ]