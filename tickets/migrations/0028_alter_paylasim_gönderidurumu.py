# Generated by Django 4.0.4 on 2022-06-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0027_paylasim_sssmi_alter_paylasim_gönderidurumu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='gönderiDurumu',
            field=models.BooleanField(default=False),
        ),
    ]
