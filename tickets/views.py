from datetime import date
from genericpath import exists
from operator import ge
from unicodedata import category
from . models import Category, Paylasim, Ariza, Firma
from django.shortcuts import redirect, render
from django.db.models import F


def arizakayit(request):
    if request.method == 'POST':
        gelenMail1 = request.POST['gelenMail']
        gelenAdSoyad1 = request.POST['gelenAdSoyad']
        gelenTelefon1 = request.POST['gelenTelefon']
        gelenAciklama1 = request.POST['gelenAciklama']
        gelenKonu1 = request.POST['gelenKonu']
        FirmaName1=request.POST['firmaismi']
        if Firma.objects.filter(FirmaName=FirmaName1).exists():
            firmaid = Firma.objects.get(FirmaName=FirmaName1)         
            gelenValues = Ariza(gelenMail=gelenMail1, gelenAdSoyad=gelenAdSoyad1,
                            gelenTelefon=gelenTelefon1, gelenKonu=gelenKonu1, gelenAciklama=gelenAciklama1,firma_bilgi_id=firmaid.id)
        else:
            firmaValues=Firma(FirmaName =FirmaName1 )
            firmaValues.save()
            firmaid = firmaValues.id
            gelenValues = Ariza(gelenMail=gelenMail1, gelenAdSoyad=gelenAdSoyad1,
                                gelenTelefon=gelenTelefon1, gelenKonu=gelenKonu1, gelenAciklama=gelenAciklama1,firma_bilgi_id=firmaid)
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
        "category": Category.objects.filter(UrunTip="came"),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "came.html", data)


def cameCategory(request, slug):
    data2 = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=True, category__slug=slug,yazılımUrunumu=False),
        "category": Category.objects.filter(UrunTip="came"),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "came.html", data2)




def yazilim(request):
    data3={
        "paylasimlar":Paylasim.objects.filter(yazılımUrunumu=True),
        "category": Category.objects.filter(UrunTip="yazılım"),
        "paylasimlarall": Paylasim.objects.all(),
    }

    return render(request,"yazilim.html", data3)

def yazılımCategory(request, slug):
    data2 = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=False, category__slug=slug,yazılımUrunumu=True),
        "category": Category.objects.filter(UrunTip="yazılım"),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "yazilim.html", data2)    

def arizalar(request):

    if request.user.is_authenticated:

        arizalar = {
            "arizalar": Ariza.objects.all(),
            "date": Ariza.objects.annotate(authors__name=F('last_update')),
            "arizaSayi": Ariza.objects.count(),
            "firmalar": Firma.objects.all(),
            "firmaSayi": Firma.objects.aggregate(),

        }
        print(date)
        return render(request, "arizalar.html", arizalar)
    else:
        return redirect("tickets")

def arızaFirma(request,slug):
    if request.user.is_authenticated:
        arizalar={
            "arizalar":Ariza.objects.filter(firma_bilgi__slug=slug),
            "firmalar": Firma.objects.all(),
        }
        return render(request,"arizalar.html",arizalar)
    else:
        return redirect("tickets")

def arizaDetay(request, slug):
    detayid = Ariza.objects.get(slug=slug)
    return render(request, "arizaDetay.html", {"detayid": detayid})
    