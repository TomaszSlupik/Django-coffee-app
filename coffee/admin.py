from dataclasses import field
from msilib.schema import Class
from django.contrib import admin
from .models import Coffee

@admin.register (Coffee)
class CoffeeAdmin (admin.ModelAdmin):
    fields =['name', 'description', 'typecoffee', 'zdjecia']
