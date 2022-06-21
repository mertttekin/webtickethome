from django import views
from django.urls import URLPattern, path
from .views import ariza_list


urlpatterns = [
    path('arizalar/', ariza_list)
]
