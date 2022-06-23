from asyncio.windows_events import NULL
from datetime import date
from distutils.log import error
from email import message
from genericpath import exists
from itertools import count
from operator import ge
from tkinter import E
from unicodedata import category

from django.http import HttpResponse, HttpResponseRedirect
from . models import Category, Paylasim, Ariza, Firma, Comment, User
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import F
from .forms import ProductCreateForm, ArizaCevapForm, ArizaGönder, FirmaGönder, CommentForm
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def arizakayit(request, **kwargs):
    if request.method == 'POST':
        form = ArizaGönder(request.POST)
        firmaform = FirmaGönder(request.POST or None)
        if firmaform.is_valid():
            FirmaName1 = firmaform.cleaned_data['FirmaName']
            print(FirmaName1)
            if FirmaName1 == None and form.is_valid():
                form.save()
                messages.success(
                    request, "Firma Girilmeden Gönderildi")
                return redirect("tickets")

            elif Firma.objects.filter(FirmaName=FirmaName1.upper()).exists() and form.is_valid():
                print('Bu Firma Mevcut')
                firmaid = Firma.objects.filter(FirmaName=FirmaName1.upper())
                ids = firmaid.values_list('pk', flat=True)
                print(ids[0])
                form1 = form.save(commit=False)
                form1.firma_bilgi_id = ids[0]
                form1.save()
                messages.success(
                    request, "Sistemde Kayıtlı olan Bir Firma Adına Arıza Gönderildi")
                return redirect("tickets")

            elif form.is_valid():
                firmaform.save()
                firmaid = Firma.objects.filter(FirmaName=FirmaName1.upper())
                ids = firmaid.values_list('pk', flat=True)
                form1 = form.save(commit=False)
                print(ids[0])
                form1.firma_bilgi_id = ids[0]
                form1.save()
                #send_mail("Ariza Mesajı alındı", message, from_email, ['admin@example.com'])
                messages.success(
                    request, "Yeni Bir Firma Adına Arıza talebi gönderildi")
                return redirect("tickets")

        else:
            messages.error(request, "Büyük Bir hata oluştu")
            return redirect("tickets")
    firmaform = FirmaGönder()
    form = ArizaGönder()
    data = {
        "paylasimlarall": Paylasim.objects.all()[:5],
        "arizalar": Ariza.objects.all(),
        "form": form,
        "firmaform": firmaform
    }
    return render(request, "tickets.html", data)


def home(request):

    data = {
        "paylasimlarall": Paylasim.objects.all()[:2],
        "arizalar": Ariza.objects.all(),
        "sliders": [
            {
                "slider_image": "slider-foto-1.png"
            },
            {
                "slider_image": "slider-foto-2.png"
            }
        ]
    }
    return render(request, "index.html", data)

# kullanılmayan bir fonksiyon (tickets)+++++


def tickets(request):
    data = {
        "paylasimlarall": Paylasim.objects.all()[:3],
        "arizalar": Ariza.objects.all(),
    }
    return render(request, "tickets.html", data)


def details(request, slug):
    detayid = Paylasim.objects.get(slug=slug)

    return render(request, "details.html", {"detayid": detayid})


def came(request):
    data = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=True, gönderiDurumu=True),
        "category": Category.objects.filter(UrunTip="came"),
        "paylasimlarall": Paylasim.objects.all()[:10],
    }
    return render(request, "came.html", data)


def cameCategory(request, slug):
    data2 = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=True, category__slug=slug, yazılımUrunumu=False),
        "category": Category.objects.filter(UrunTip="came"),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "came.html", data2)


def yazilim(request):
    data3 = {
        "paylasimlar": Paylasim.objects.filter(yazılımUrunumu=True, gönderiDurumu=True),
        "category": Category.objects.filter(UrunTip="yazılım"),
        "paylasimlarall": Paylasim.objects.all(),
    }

    return render(request, "yazilim.html", data3)


def yazılımCategory(request, slug):
    data2 = {
        "paylasimlar": Paylasim.objects.filter(cameUrunumu=False, category__slug=slug, yazılımUrunumu=True),
        "category": Category.objects.filter(UrunTip="yazılım"),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "yazilim.html", data2)


def arizalar(request):

    if request.user.is_authenticated:

        arizalar = {
            "arizalar": Ariza.objects.order_by('-create_time').filter(Arsivmi=False),
            "arizaSayi": Ariza.objects.filter(Arsivmi=False).count(),
            "firmalar": Firma.objects.order_by('FirmaName').filter(ariza__Arsivmi=False).distinct(),
            "firmaSayi": Firma.objects.count(),
            #        Article.objects.filter(reporter__first_name='John')
            #     QuerySet [<Article: John's second story>, <Article: This is a test>]>

        }
        return render(request, "arizalar.html", arizalar)
    else:
        return redirect("tickets")


def arızaFirma(request, slug):
    if request.user.is_authenticated:
        arizalar = {
            "arizalar": Ariza.objects.order_by('-create_time').filter(Arsivmi=False, firma_bilgi__slug=slug),
            "firmalar": Firma.objects.order_by('FirmaName').filter(ariza__Arsivmi=False).distinct(),
            "firmabaslink2": Firma.objects.get(slug=slug),
        }

        return render(request, "arizalar.html", arizalar)
    else:
        return redirect("tickets")


def arizaDetay(request, slug):
    if request.user.is_authenticated:
        template_name = 'arizaDetay.html'
        hangi_ariza = get_object_or_404(Ariza, slug=slug)
        comments = hangi_ariza.comments.filter(active=True)
        new_comment = None
        if request.method == "POST":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                hangi_ariza.CozumVarMı = True
                new_comment = comment_form.save(commit=False)
                new_comment.hangi_ariza = hangi_ariza
                hangi_ariza.save()
                new_comment.save()
                return redirect("arizalar")
        else:
            comment_form = CommentForm()

        detayid = Ariza.objects.get(slug=slug)
        return render(request, template_name, {
            "detayid": detayid,
            'post': hangi_ariza,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,

        })

    else:
        return redirect("tickets")


def yorumSil(request, id):
    if request.user.is_authenticated:
        comments = {
            "yorumlar": Comment.objects.filter(id=id).delete(),

        }
        return redirect("paylasimgir")
    else:
        return redirect("tickets")


def paylasimgir(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductCreateForm(request.POST, request.FILES)
            print("obje kayot")
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Paylaşım yapılmıştır", extra_tags="success")
                return redirect("paylasimgir")
            else:
                messages.error(request, "Bir hata oluştu")
                print(form.errors.as_data())
        form = ProductCreateForm()
        print("yeni girdi")
        data = {
            "paylasimlarall": Paylasim.objects.all(),
            "form": form,
        }
        return render(request, "paylasimgir.html", data)
    else:
        return redirect("tickets")


def editt(request, slug):
    if request.user.is_authenticated:
        form = get_object_or_404(Paylasim, slug=slug)
        if request.method == 'POST':
            form = ProductCreateForm(
                request.POST, request.FILES, instance=form)

            if form.is_valid():
                form.save()
                return redirect("paylasimgir")
            else:
                # here you print errors to terminal
                print(form.errors.as_data())
        else:
            form = ProductCreateForm(instance=form)
        data = {
            "paylasimlarall": Paylasim.objects.filter(slug=slug),
            "form": form,
        }
        return render(request, "paylasimgir.html", data)
    else:
        return redirect("tickets")


def ArsiveEkle(request, slug):
    if request.user.is_authenticated:
        form = get_object_or_404(Ariza, slug=slug)
        if form.Arsivmi == False:
            messages.success(request, form.gelenKonu)
            form.Arsivmi = True
            form.save()

            print("test")
            return redirect("arizalar")

        data2 = {
            "arizalar": Ariza.objects.get(slug=slug),
            "form": form,
        }
        return render(request, "arsivekaldir.html", data2)
    else:
        return redirect("tickets")


def arsiv(request):
    if request.user.is_authenticated:
        arizalar = {
            "arizalar": Ariza.objects.order_by('-create_time').filter(Arsivmi=True),
            "arizaSayi": Ariza.objects.filter(Arsivmi=True).count(),
            "firmalar": Firma.objects.order_by('FirmaName').filter(ariza__Arsivmi=True).distinct(),
            "firmaSayi": Firma.objects.count(),
            #        Article.objects.filter(reporter__first_name='John')
            #     QuerySet [<Article: John's second story>, <Article: This is a test>]>

        }
        return render(request, "arsiv.html", arizalar)
    else:
        return redirect("tickets")


def arsivFirma(request, slug):
    if request.user.is_authenticated:
        arizalar = {
            "arizalar": Ariza.objects.order_by('-create_time').filter(Arsivmi=True, firma_bilgi__slug=slug),
            "firmalar": Firma.objects.order_by('FirmaName').filter(ariza__Arsivmi=True).distinct(),
            "firmabaslink2": Firma.objects.get(slug=slug),
        }

        return render(request, "arsiv.html", arizalar)
    else:
        return redirect("tickets")


def arsivdenCikar(request, slug):
    if request.user.is_authenticated:
        form = get_object_or_404(Ariza, slug=slug)
        if form.Arsivmi == True:
            form.Arsivmi = False
            form.save()
            messages.success(request, form.gelenKonu)
            print("test")
            return redirect("arsiv")

        data2 = {
            "arizalar": Ariza.objects.get(slug=slug),
            "form": form,
        }
        return render(request, "arsivekaldir.html", data2)
    else:
        return redirect("tickets")


def sss(request):
    data = {
        "sss": Paylasim.objects.filter(sssmi=True, gönderiDurumu=True),
        "paylasimlarall": Paylasim.objects.all(),
    }
    return render(request, "sss.html", data)


def post_search(request):

    return render(request, 'arama.html')


def paylasimSil(request, slug):
    if request.user.is_authenticated:
        data = {
            "paylasim": Paylasim.objects.filter(slug=slug).delete(),
        }
        messages.warning(request, "Paylasım Silinmiştir", extra_tags="warning")
        return redirect("paylasimgir")

    else:
        return redirect("tickets")


# def Firmasay():
#     arizalar = {"arizalar":Ariza.objects.all()}
#     firmalar = {"firmalar":Firma.objects.all()}
#     a=0
#     for fi in firmalar:
#         for ar in arizalar:
#             if fi.id == ar.firma_bilgi_id:
#                 a=a+1
#     firmaSayı = a
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
