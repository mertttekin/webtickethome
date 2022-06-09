import re
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def login_request(request):
    if request.user.is_authenticated:
        return redirect("arizalar")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("arizalar")
        else:
            return render(request, "account/login.html", {"error": "kullanıcı adı veya parlola hatalı"})

    return render(request, "account/login.html")


def register_request(request):
    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("tickets")
