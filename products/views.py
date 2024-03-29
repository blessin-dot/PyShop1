from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

"""
render: function used to render a template
"""
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new_products(request):
    return HttpResponse('New Products')
