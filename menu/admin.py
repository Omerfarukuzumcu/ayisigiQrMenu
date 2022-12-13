from django.contrib import admin

# Register your models here.

from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ("productName", "description", "price", "category")

admin.site.register(Menu,MenuAdmin)
