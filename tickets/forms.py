from dataclasses import field
from pyexpat import model
from tkinter import Widget
from turtle import width
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import  widgets
from django import forms
from tickets.models import Paylasim


# class ProductCreateForm(forms.Form):
#     göndericiAdi= forms.CharField(label='Your name',max_length=100)
#     gönderiKonu= forms.CharField()
#     gönderiAciklama= forms.Textarea()
#     gönderiFoto= forms.ImageField(label='foto name')
#     gönderiDurumu= forms.BooleanField(required=False)
#     yazılımUrunumu= forms.BooleanField(required=False)
#     cameUrunumu= forms.BooleanField(required=False)
#     sssmi= forms.BooleanField(required=False)


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Paylasim
        fields= "__all__"
        error_messages ={
            "göndericiAdi":{
                "required":"isim giriniz",
            }
        }
        labels={
            "göndericiAdi":"Gönderici Adı",
            "gönderiKonu":"Konu",
        }
        widgets= {
            "göndericiAdi": widgets.TextInput(attrs={"class":"form-control"}),
            "gönderiKonu": widgets.TextInput(attrs={"class":"form-control"}),
        }