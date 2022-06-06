from asyncio.windows_events import NULL
from datetime import date
from genericpath import exists
from operator import ge
from unicodedata import category
from . models import Category, Paylasim, Ariza, Firma
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import F
from .forms import ProductCreateForm

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
        "paylasimlarall": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "tickets.html", data)


def home(request):
    data = {
        "paylasimlarall": Paylasim.objects.all(),
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "index.html", data)

# kullanılmayan bir fonksiyon (tickets)


def tickets(request):
    data = {
        "paylasimlarall": Paylasim.objects.all(),
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
            "arizalar": Ariza.objects.order_by('-create_time'),
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
    if request.user.is_authenticated:
        detayid = Ariza.objects.get(slug=slug)
        return render(request, "arizaDetay.html", {"detayid": detayid})
    else:
        return redirect("tickets")


def paylasimgir(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductCreateForm(request.POST, request.FILES)
            print("obje kayot")
            if form.is_valid():
                form.save()
                return redirect("paylasimgir")
            else:
                print(form.errors.as_data()) # here you print errors to terminal
        form=ProductCreateForm()
        print("yeni girdi")
        data = {
            "paylasimlarall": Paylasim.objects.all(),
            "form":form,
    }
        return render(request,"paylasimgir.html",data) 
    else:
        return redirect("tickets")       

def editt(request,slug):
    if request.user.is_authenticated:
        form = get_object_or_404(Paylasim, slug=slug)
        if request.method == 'POST':
            form = ProductCreateForm(request.POST, request.FILES,instance=form)
            
            if form.is_valid():
                form.save()
                return redirect("paylasimgir")
            else:
                print(form.errors.as_data()) # here you print errors to terminal
        else:        
            form=ProductCreateForm(instance=form)
        data = {
            "paylasimlarall": Paylasim.objects.filter(slug=slug),
            "form":form,
              }
        return render(request,"paylasimgir.html",data) 
    else:
        return redirect("tickets")    



# def paylasimgir(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             göndericiAdi1=request.POST['göndericiAdi']
#             gönderiKonu1=request.POST['gönderiKonu']
#             gönderiAcıklama1=request.POST['gönderiAcıklama']
#             gönderiFoto1=request.FILES.get('images')
#             gönderiDurumu1=request.POST.get('gönderiDurumu',False)
#             gönderiCameUrunumu1=request.POST.get('gönderiCameUrunumu',False)
#             gönderiYazılımUrunumu1=request.POST.get('gönderiYazılımUrunumu',False)
#             gönderiSSSmi1=request.POST.get('gönderiSSSmi',False)
#             categoryid = Category.objects.get(id=2) 

#             gönderiObject.save()    
#             return render(request, "paylasimgir.html" ,{"success": "kullanıcı adı veya parlola hatalı"})
#         data2 = {
#             "paylasimlarall": Paylasim.objects.all(),
#         }
#         return render(request,"paylasimgir.html",data2)
#     else:
#         return redirect("tickets")