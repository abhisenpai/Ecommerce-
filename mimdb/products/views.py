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


def single_product(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        products=Product.objects.all()
        template = 'products/single.html'
        context = {'product':product}
        return render(request,template,context)
    except:
        pass
def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=None
    if q:
        products = Product.objects.filter(title__icontains=q)
        template='products/results.html'
        context={'query':q,'products':products}
    else:
        template='products/home.html'
        context={}
            
    return render(request,template,context)
