# Generated by Django 3.2.9 on 2021-12-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0026_alter_equipo_licencia_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='puerto_ssh',
            field=models.CharField(default='', max_length=255),
        ),
    ]
