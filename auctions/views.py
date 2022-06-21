from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    prod_names = list(products.values('product_name'))
    cats = list(products.values('category'))
    C = []
    for i in cats:
        cat = list(i.values())
        C.append(cat)
    N = []
    for i in prod_names:
        prod = list(i.values())
        N.append(prod)
    names=[]
    for i in N:
        for j in i:
            names.append(j)
    print(names)
    categories = []
    for i in C:
        for j in i:
            categories.append(j)

    item = {'products':names, 'category':categories}
    return render(request, 'auctions/index.html',item)


def login(request):
    return render(request, 'auctions/login.html')


def items(request,title):
    return render(request, 'auctions/items.html',{'item':title})


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    return render(request, 'auctions/contact.html')
    