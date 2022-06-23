from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.views import View
from . import views


urlpatterns = [
    path('', views.arizakayit, name="tickets"),
    path('home/', views.home, name="home"),
    path('tickets/', views.arizakayit, name="tickets"),
    path('details/<slug:slug>', views.details, name="details"),
    path('came/', views.came, name="came"),
    path('came/<slug:slug>', views.cameCategory, name="cameCategory"),
    path('arizalar/', views.arizalar, name="arizalar"),
    path('yazilim/', views.yazilim, name="yazilim"),
    path('yazilim/<slug:slug>', views.yazılımCategory, name="yazılımCategory"),
    path('arizalar/<slug:slug>', views.arızaFirma, name="arızaFirma"),
    path('ariza/detay/<slug:slug>', views.arizaDetay, name="arizaDetay"),
    path('paylasimgir/', views.paylasimgir, name="paylasimgir"),
    path('paylasimgir/editt/<slug:slug>', views.editt, name="editt"),
    path('arizalar/arsiv/ekle/<slug:slug>',
         views.ArsiveEkle, name="ArsiveEkle"),
    path('arsiv/', views.arsiv, name="arsiv"),
    path('arsiv/<slug:slug>', views.arsivFirma, name="arsivFirma"),
    path('arsiv/arsivdencikar/<slug:slug>',
         views.arsivdenCikar, name="arsivdenCikar"),
    path('sss', views.sss, name="sss"),
    path('paylasimgir/sil/<slug:slug>', views.paylasimSil, name="paylasimSil"),
    path('ariza/detaysil/<int:id>',
         views.yorumSil, name="yorumSil"),

]
# path(url,foksiyon,path ismi)
