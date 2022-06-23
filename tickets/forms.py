from dataclasses import field, fields
from email.policy import default
from pyexpat import model
from tkinter import Widget
from turtle import width
from urllib import request
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import widgets
from django import forms
from tickets import models
from tickets.models import Ariza, Firma, Paylasim, Comment
from ckeditor.fields import RichTextField
from django.db import models


# class ProductCreateForm(forms.Form):
#     göndericiAdi= forms.CharField(label='Your name',max_length=100)
#     gönderiKonu= forms.CharField()
#     gönderiAciklama= forms.Textarea()
#     gönderiFoto= forms.ImageField(label='foto name')
#     gönderiDurumu= forms.BooleanField(required=False)
#     yazılımUrunumu= forms.BooleanField(required=False)
#     cameUrunumu= forms.BooleanField(required=False)
#     sssmi= forms.BooleanField(required=False)

class ArizaGönder(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = "__all__"
        exclude = [
            'slug',
            'CozumVarMı',
            'Arsivmi',
            'firma_bilgi',
        ]

        widgets = {
            "firma_bilgi": widgets.Select(attrs={"class": "form-control"}),
            "gelenKonu": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Kamera Görüntüsü Gelmiyor"}),
            "gelenMail": widgets.EmailInput(attrs={"class": "form-control", "placeholder": "mert.tekin@aksiyonteknoloji.com"}),
            "gelenAdSoyad": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Mert TEKİN"}),
            "gelenTelefon": widgets.NumberInput(attrs={"class": "form-control", "placeholder": "(216) 999 9559"}),
            "gelenAciklama": widgets.Textarea(attrs={"class": "form-control", "placeholder": "Açıklama..."}),

        }

        labels = {
            "gelenAdSoyad": "Ad Soyad",
            "gelenKonu": "Konu",
            "gelenMail": "Email Adresi Giriniz",
            "gelenTelefon": "İrtibat Telefonu",
            "gelenAciklama": "Açıklama",
            "firma_bilgi": "Firma Seç",
        }

    def __init__(self, *args, **kwargs):
        super(ArizaGönder, self).__init__(*args, **kwargs)
        self.fields['firma_bilgi'].required = False

    def __init__(self, *args, **kwargs):
        super(ArizaGönder, self).__init__(*args, **kwargs)
        self.fields['gelenAciklama'].required = True


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Paylasim
        fields = "__all__"
        error_messages = {

            "gönderiKonu": {
                "required": "Konu Giriniz",
            },
            "gönderiAciklama": {
                "required": "Açıklama Giriniz",
            },
            "gönderiFoto": {
                "required": "Açıklama Giriniz",
            },

        }
        labels = {
            "göndericiAdi": "Gönderici Adı",
            "gönderiKonu": "Konu",
            "gönderiFoto": "Görsel Ekleyiniz",
            "gönderiDurumu": "Paylaşımınız yayınlansın mı ?",
            "yazılımUrunumu": "Yazılım sayfası altında mı yayınlansın ?",
            "cameUrunumu": "Came sayfası altında mı yayınlansın ?",
            "sssmi": "S.S.S. sayfası altında mı yayınlansın ?",
            "category": "Hangi kategori altında yayınlansın ?",
            "gönderiAciklama": "Bir açıklama Giriniz",
        }
        widgets = {
            "göndericiAdi": widgets.TextInput(attrs={"class": "form-control"}),
            "gönderiKonu": widgets.TextInput(attrs={"class": "form-control"}),
            "gönderiFoto": widgets.FileInput(attrs={"class": "form-control"}),
            "gönderiDurumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "yazılımUrunumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "cameUrunumu": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "sssmi": widgets.NullBooleanSelect(attrs={"class": "form-control"}),
            "category": widgets.Select(attrs={"class": "form-control"}),
            "gönderiAciklama": widgets.Textarea(attrs={
                'class': 'form-control django-ckeditor-widget ckeditor',
                'id': 'form-control',
                'spellcheck': 'False'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = True

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['göndericiAdi'].required = True

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['gönderiKonu'].required = True


class ArizaCevapForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ['CozumVarMı']


class ArizaArsiv(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ['Arsivmi']
        Arsivmi = True


class FirmaGönder(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ['FirmaName']

        labels = {
            "FirmaName": "Firma Adı Giriniz",
        }
        widgets = {
            "FirmaName": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Aksiyon Teknoloji Hizmetleri"}),
        }

    def __init__(self, *args, **kwargs):
        super(FirmaGönder, self).__init__(*args, **kwargs)
        self.fields['FirmaName'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('yorum',)
        labels = {
            "yorum": "Uygulanan çözümü ayrıntılı yazmayı unutmayınız",
        }
        widgets = {
            "yorum": widgets.Textarea(attrs={"class": "form-control", "placeholder": ""}),
        }
