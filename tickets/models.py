from collections import UserList
from datetime import date
from email.policy import default
from sqlite3 import Timestamp
from turtle import mode, st, update
from unicodedata import category
from venv import create
from xml.parsers.expat import model
from django.conf import UserSettingsHolder
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from PIL import Image
from django.contrib.auth.models import User
from django.db.models import Count
from pkg_resources import safe_name


class Status(models.Model):
    name = models.CharField(max_length=100)

# gelenFoto/1.jpeg
# göndericiFoto/1.jpeg


class Firma(models.Model):
    FirmaName = models.CharField(max_length=100, default="Firmasız")
    FirmaYetkilisi = models.CharField(max_length=50, null=True, blank=True)
    FirmaİletisimMail = models.CharField(max_length=50, null=True, blank=True)
    FirmaİletisimTelefon = models.CharField(
        max_length=50, null=True, blank=True)
    #FirmaSayısı = Ariza.objects.aggregate(total_count=Count('id'))

    slug = models.SlugField(null=False,
                            db_index=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.FirmaName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.FirmaName)
        super().save(*args, **kwargs)


class Ariza(models.Model):

    gelenMail = models.CharField(max_length=50)
    #gelenFoto = models.ImageField(upload_to="Arizas")
    gelenAdSoyad = models.CharField(max_length=50)
    gelenTelefon = models.CharField(max_length=50)
    gelenKonu = models.CharField(max_length=50)
    gelenAciklama = RichTextField()
    slug = models.SlugField(null=True,
                            db_index=True, blank=True, editable=False, unique=True)
    firma_bilgi = models.ForeignKey(
        Firma, null=True, on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    ArizaCozumu = RichTextField(default="Girilmedi")
    Arsivmi = models.BooleanField(default=False)
    #gelenFirma = models.CharField(max_length=50, default="Belirtilmemiş")
    # slug = models.SlugField(null=True, unique=True, db_index=True)
    # önce null False olursa migrationda sorun çıkıyor önce true ile nullar doldurulup sonra false çevirilmeli

    def __str__(self):
        return f"{self.gelenAdSoyad}"

    def save(self, *args, **kwargs):
        super(Ariza, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.gelenKonu) + "-" + str(self.id)
            self.save()


class Category(models.Model):
    categoryName = models.CharField(max_length=100, default="Genel")
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    UrunTip = models.CharField(max_length=100, default="came")

    def __str__(self):
        return f"{self.categoryName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)


class Paylasim(models.Model):
    göndericiAdi = models.CharField(max_length=100)
    gönderiKonu = models.CharField(max_length=100)
    gönderiAciklama = RichTextField()
    gönderiFoto = models.ImageField(
        upload_to="Paylasim/", blank=True, null=True, default="Paylasim/akslogo.png")
    gönderiDurumu = models.BooleanField(default=False)
    yazılımUrunumu = models.BooleanField(default=False)
    cameUrunumu = models.BooleanField(default=False)
    sssmi = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, editable=True, default=9)
    göndericiUser = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, editable=False)

    def __str__(self):
        return f"{self.gönderiKonu}"

    def save(self, *args, **kwargs):
        super(Paylasim, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.gönderiKonu) + "-" + str(self.id)
            self.save()
