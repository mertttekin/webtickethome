from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('tickets/', views.arizakayit, name="tickets"),
    path('details/<slug:slug>', views.details, name="details"),
    path('came/', views.came, name="came"),
]

# path(url,foksiyon,path ismi)
