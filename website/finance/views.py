from django.shortcuts import render
from .models import Konto, Umsatz, Budget

def home(request):
    saldo=Konto.objects.all()
    return render(request, "home.html", {'saldo':saldo})


def about(request):
    return render(request, "about.html")

def createbudget(request):
    return render(request, "createbudget.html")

def contact(request):
    return render(request, "contact.html")

def umsatz(request):
    umsatz=Umsatz.objects.all().order_by('-id')[:25]

    return render(request, "umsatz.html", {'umsatz':umsatz})

def budget(request):
    budget=Budget.objects.all().order_by('-id')
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('budget'):
            budget=Budget()
            budget.name=request.POST.get('name')
            budget.budget=request.POST.get('budget')
            budget.save()

            return render(request, 'budget.html')
    else:
        return render(request, 'budget.html', {'budget':budget})

    return render(request, "budget.html")