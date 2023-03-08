# Generated by Django 4.1.6 on 2023-02-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0008_alter_reserva_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='turno',
            field=models.CharField(choices=[('manhã', 'Manhã'), ('tarde', 'Tarde')], default='não especificado', max_length=10, null=True, verbose_name='Turno'),
        ),
    ]
