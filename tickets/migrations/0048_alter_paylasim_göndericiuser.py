# Generated by Django 4.0.4 on 2022-06-12 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0047_alter_ariza_firma_bilgi_alter_ariza_gelenaciklama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='göndericiUser',
            field=models.ForeignKey(default=5, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
