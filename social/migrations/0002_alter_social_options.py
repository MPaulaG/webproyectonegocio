# Generated by Django 4.1.3 on 2022-11-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'ordering': ['name'], 'verbose_name': 'red social', 'verbose_name_plural': 'Redes Sociales'},
        ),
    ]
