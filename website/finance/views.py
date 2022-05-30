from django.shortcuts import render
from .models import Konto, Umsatz

def home(request):
    saldo=Konto.objects.all()
    return render(request, "home.html", {'saldo':saldo})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def umsatz(request):
    umsatz=Umsatz.objects.all().order_by('-datum')

    return render(request, "umsatz.html", {'umsatz':umsatz})