# Generated by Django 3.2.9 on 2021-11-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('servicio', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('ip_cliente', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('puerto', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('ci', models.CharField(max_length=255)),
            ],
        ),
    ]
