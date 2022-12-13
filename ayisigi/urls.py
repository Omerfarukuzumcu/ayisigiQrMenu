"""ayisigi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('firinurunleri/', views.Firinurunleri, name = 'Firinurunleri'),
    path('sandvicler/', views.Sandvicler, name = 'Sandvicler'),
    path('tatlilar/', views.Tatlılar, name = 'Tatlılar'),
    path('serbetlitatlilar/', views.SerbetliTatlilar, name = 'SerbetliTatlilar'),
    path('adeturunler/', views.AdetUrunler, name = 'AdetUrunler'),
    path('kahvalti/', views.Kahvalti, name = 'Kahvalti'),
    path('mezeler/', views.Meze, name = 'Mezeler'),
    path('borekler/', views.Borekler, name = 'Borekler'),
    path('icecekler/', views.Icecekler, name = 'Icecekler'),     
    
]
