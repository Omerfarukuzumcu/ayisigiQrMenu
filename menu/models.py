from django.db import models

# Create your models here.


class Menu(models.Model):
    CHOICES = (
        ("FırınUrunleri", "Fırın Ürünleri"),
        ("AdetUrunleri", "Adet Ürünler"),
        ("Borek", "Börek"),
        ("Icecek", "İçecek"),
        ("Kahvalt", "Kahvaltı"),
        ("Sandvic", "Sandvic"),
        ("Meze", "Meze"),
        ("Tatlı", "Tatlı"),
        ("SerbetliTatlı", "Şerbetli Tatlı"),
    )
    productName = models.CharField(max_length=100)
    description = models.CharField(max_length=150,blank=True)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CHOICES)

    