# Generated by Django 4.0.4 on 2022-05-30 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_ariza_gelenkonu_alter_paylasim_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ariza',
            name='slug',
        ),
    ]
