from django.shortcuts import render
from .models import News

def home(request):

    obj = News.objects.all()

    context = {"object":obj}

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")