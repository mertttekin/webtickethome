# Generated by Django 4.0.4 on 2022-05-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_remove_ariza_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
