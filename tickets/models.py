from turtle import mode
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)


class Ariza(models.Model):

    gelenMail = models.CharField(max_length=50)
    gelenAdSoyad = models.CharField(max_length=50)
    gelenTelefon = models.CharField(max_length=50)
    gelenAciklama = models.TextField()


class Paylasim(models.Model):
    göndericiAdi = models.CharField(max_length=100)
    gönderiKonu = models.CharField(max_length=100)
    gönderiAciklama = models.TextField()
    gönderiDurumu = models.BooleanField(default=False)
    cameUrunumu = models.BooleanField(default=False)
