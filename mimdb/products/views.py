from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all()
    template='products/home.html'
    context={'products':products}
    return render(request,template,context)

def all(request):
    template = 'products/all.html'
    context = {'products':Product.objects.all()}
    return render(request,template,context)