# Generated by Django 4.0.5 on 2022-06-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0057_alter_ariza_gelentelefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ariza',
            name='gelenTelefon',
            field=models.IntegerField(),
        ),
    ]
