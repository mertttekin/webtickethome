from operator import ge
from unicodedata import category
from . models import Category, Paylasim, Ariza, Firma
from django.shortcuts import redirect, render


def arizakayit(request):
    if request.method == 'POST':
        gelenMail1 = request.POST['gelenMail']
        gelenAdSoyad1 = request.POST['gelenAdSoyad']
        gelenTelefon1 = request.POST['gelenTelefon']
        gelenAciklama1 = request.POST['gelenAciklama']
        gelenKonu1 = request.POST['gelenKonu']
        gelenValues = Ariza(gelenMail=gelenMail1, gelenAdSoyad=gelenAdSoyad1,
                            gelenTelefon=gelenTelefon1, gelenKonu=gelenKonu1, gelenAciklama=gelenAciklama1)
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


def details(request, slug):
    detayid = Paylasim.objects.get(slug=slug)
    detay = {
        "paylasimlar": Paylasim.objects.all(),
    }
    return render(request, "details.html", {"detayid": detayid})


def came(request):
    data = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=True),
        "category": Category.objects.all(),
    }
    return render(request, "came.html", data)


def cameCategory(request, slug):
    data2 = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=True, category__slug=slug),
        "category": Category.objects.all(),
    }
    return render(request, "came.html", data2)


def arizalar(request):

    if request.user.is_authenticated:

        arizalar = {
            "arizalar": Ariza.objects.all(),
            "arizaSayi": Ariza.objects.count(),
            "firmalar": Firma.objects.all(),
            "firmaSayi": Firma.objects.aggregate(),

        }

        return render(request, "arizalar.html", arizalar)
    else:
        return redirect("tickets")
