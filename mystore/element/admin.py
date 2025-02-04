from django.contrib import admin
from .models import Category, Type, Element

# Register your models here.

@admin.register(Category, Type)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

    

@admin.display(description="Id and title in UPPER Case")
def upper_title(obj):
    return f"{obj.id} - {obj.title}".upper()

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'type', upper_title)
    #fields =(('title', 'slug'), 'description', 'price', 'category', 'type')
    fieldsets = [
        (
    "Regular Options",
    {
        "fields":(('title', 'slug'), 'description', 'category', 'type')
    }
        ),
    (
    "Advanced Options",
    {
        "fields":('price',)
    }
        ),
    ]