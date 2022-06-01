from turtle import mode, update
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Status(models.Model):
    name = models.CharField(max_length=100)

# gelenFoto/1.jpeg
# göndericiFoto/1.jpeg


class Ariza(models.Model):

    gelenMail = models.CharField(max_length=50)
    #gelenFoto = models.ImageField(upload_to="Arizas")
    gelenAdSoyad = models.CharField(max_length=50)
    gelenTelefon = models.CharField(max_length=50)
    gelenKonu = models.CharField(max_length=50)
    gelenAciklama = RichTextField()
    # slug = models.SlugField(null=True, unique=True, db_index=True)
    # önce null False olursa migrationda sorun çıkıyor önce true ile nullar doldurulup sonra false çevirilmeli

    def __str__(self):
        return f"{self.gelenAdSoyad}"


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.categoryName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)


class Paylasim(models.Model):
    göndericiAdi = models.CharField(max_length=100)
    gönderiKonu = models.CharField(max_length=100)
    gönderiAciklama = RichTextField()
    gönderiFoto = models.ImageField(upload_to="Paylasim")
    gönderiDurumu = models.BooleanField(default=False)
    cameUrunumu = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True,
                            db_index=True, blank=True, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gönderiKonu}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.gönderiKonu)
        super().save(*args, **kwargs)
