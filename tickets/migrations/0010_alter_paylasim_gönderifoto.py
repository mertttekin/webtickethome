# Generated by Django 4.0.4 on 2022-05-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_paylasim_gönderifoto_alter_paylasim_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='gönderiFoto',
            field=models.CharField(max_length=50),
        ),
    ]
