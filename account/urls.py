from django import views
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name="logout"),
]
