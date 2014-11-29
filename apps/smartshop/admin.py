from django.contrib import admin
from models import Product, NameProduct


class ProductInline(admin.TabularInline):
    model = Product
    extra = 3


class NameProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']})
    ]
    inlines = [ProductInline]

admin.site.register(NameProduct, NameProductAdmin)
admin.site.register(Product)
