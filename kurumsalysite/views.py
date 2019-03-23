from django.shortcuts import render, redirect
from .models import Contact, Makaleler

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'kurumsalysite/index.html', {'nbar' : 'index'})


def about(request):
    return render(request, 'kurumsalysite/hakkimizda.html', {'nbar' : 'about'})


def services(request):
    return render(request, 'kurumsalysite/hizmetlerimiz.html', {'nbar' : 'services'})

def process(request):
    return render(request, 'kurumsalysite/surec.html', {'nbar' : 'process'})

def faq(request):
    return render(request, 'kurumsalysite/faq.html', {'nbar' : 'faq'})

def contact(request):
    if request.method == "POST":
        adsoyad = request.POST.get('adsoyad')
        email = request.POST.get('email')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_ulasim=email, iletisim_mesaj=mesaj)
        iletisim.save()

        return redirect('/?gonder=ok')

    return render(request, 'kurumsalysite/iletisim.html', {'nbar' : 'contact'})



def articles(request):
    makale_list = Makaleler.objects.all()   ## sonra bi sn kapı caldı geliyom
    paginator = Paginator(makale_list, 6)  # Her Sayfada 1 Makale Gösterilecek.

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'kurumsalysite/makaleler.html', {'nbar' : 'articles' ,'articles' : articles})




def articledetay(request, makaleslug):
    makale = Makaleler.objects.get(makale_slug=makaleslug)
    return render(request, 'kurumsalysite/makaledetay.html', {'makale' : makale, 'nbar' : 'articledetail'})



def muvekkil(request):
    return render(request, 'kurumsalysite/muvekkil.html', {'muvekkil' : 'muvekkil', 'nbar' : 'muvekkil'})



def not_found(request):
    return render(request, 'kurumsalysite/404.html')






