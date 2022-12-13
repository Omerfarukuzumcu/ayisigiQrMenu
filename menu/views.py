from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request): 
    return render(request,"index.html")

def Firinurunleri(request):
    product = Menu.objects.filter(category="FırınUrunleri")
    context = {
        "product":product
    }
    return render(request,"Firinurunleri.html",context)

def Sandvicler(request):
    product = Menu.objects.filter(category="Sandvic")
    context = {
        "product":product
    }
    return render(request,"Sandvicler.html",context)    

def Tatlılar(request):
    product = Menu.objects.filter(category="Tatlı")
    context = {
        "product":product
    }
    return render(request,"Tatlılar.html",context)    

def SerbetliTatlilar(request):
    product = Menu.objects.filter(category="SerbetliTatlı")
    context = {
        "product":product
    }
    return render(request,"SerbetliTatlilar.html",context)    

def AdetUrunler(request):
    product = Menu.objects.filter(category="AdetUrunleri")
    context = {
        "product":product
    }
    return render(request,"AdetUrunler.html",context)    

def Kahvalti(request):
    product = Menu.objects.filter(category="Kahvalt")
    context = {
        "product":product
    }
    return render(request,"Kahvalti.html",context)    

def Meze(request):
    product = Menu.objects.filter(category="Meze")
    context = {
        "product":product
    }
    return render(request,"Meze.html",context)    

def Borekler(request):
    product = Menu.objects.filter(category="Borek")
    context = {
        "product":product
    }
    return render(request,"Borekler.html",context)    

def Icecekler(request):
    product = Menu.objects.filter(category="Icecek")
    context = {
        "product":product
    }
    return render(request,"Icecekler.html",context)    



