from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    for product in products:
        title = product.product_name
        print(title)
    item = {'products':products}
    return render(request, 'auctions/index.html', item)


def login(request):
    return render(request, 'auctions/login.html')


def items(request, id):
    product = Product.objects.get(id=id)
    specs = product.specifications.split('.')
    return render(request, 'auctions/items.html', {'product':product , 'specs': specs})


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    return render(request, 'auctions/contact.html')


def signup(request):
    return render(request, 'auctions\signup.html')
    