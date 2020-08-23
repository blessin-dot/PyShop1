from django.contrib import admin
from .models import Product, Offer

# Register your models here.


#ModelAdmin: provides functionality for managing models in the admin area
class ProductAdmin(admin.ModelAdmin):
    """
    Product class for administrations
    class that allows the admin to customizations
    """
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# we want to manage our products in the admin side
"""Django uses the second argument (ProductAdmin) to decide
how to best present the products"""
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
