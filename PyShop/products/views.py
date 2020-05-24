from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# /products -> index
def index(request):
    return HttpResponse('Hello world')


def new(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
