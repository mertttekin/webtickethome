from django.http import HttpResponseRedirect
from django.shortcuts import render
from . models import Paylasim, Ariza


def arizakayit(request):
    if request.method == 'POST':
        gelenMail1 = request.POST['gelenMail']
        gelenAdSoyad1 = request.POST['gelenAdSoyad']
        gelenTelefon1 = request.POST['gelenTelefon']
        gelenAciklama1 = request.POST['gelenAciklama']
        gelenValues = Ariza(gelenMail=gelenMail1, gelenAdSoyad=gelenAdSoyad1,
                            gelenTelefon=gelenTelefon1, gelenAciklama=gelenAciklama1)
        gelenValues.save()
        print("varan1")
        return render(request, "index.html")
    print("varan2")
    data = {
        "paylasimlar": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "tickets.html", data)


def home(request):
    data = {
        "paylasimlar": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "index.html", data)

# kullanılmayan bir fonksiyon (tickets)


def tickets(request):
    data = {
        "paylasimlar": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "tickets.html", data)


def details(request, id):
    return render(request, "details.html", {"id": id})


def came(request):
    data = {
        "paylasimlar": Paylasim.objects.all(),
    }
    return render(request, "came.html", data)
