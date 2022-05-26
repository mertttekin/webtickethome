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
    return render(request, "tickets.html")


def home(request):
    data = {
        "paylasimlar": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "index.html", data)


def tickets(request):
    data = {
        "paylasimlar": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "tickets.html", data)
