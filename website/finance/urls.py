from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('umsatz/', views.umsatz, name = 'umsatz'),
    path('budget/', views.budget, name = 'budget'),
    path('createbudget/', views.createbudget, name = 'createbudget'),
]