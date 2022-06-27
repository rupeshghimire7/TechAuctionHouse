from django.shortcuts import render, HttpResponse
from .models import Product

products = Product.objects.all()
# Create your views here.
def index(request):
    for product in products:
        title = product.product_name
    item = {'products':products}
    return render(request, 'auctions/index.html', item)


def login(request):
    return render(request, 'auctions/login.html')


def items(request, id):
    product = Product.objects.get(id=id)

    highest_bid = request.POST.get('bid_price')
#    highest_bid = float(highest_bid)
#    if highest_bid < product.price:
#       condition = True
    print(highest_bid)
    message="Invalid Bid! Your bid cannot be lower than base price. Please try another bid!"
    specs = product.specifications.split('.')
    return render(request, 'auctions/items.html', {'product':product , 'specs': specs, 'hightst_bid':highest_bid, 'message':message})


def search(request):
    pass


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    return render(request, 'auctions/contact.html')


def signup(request):
    return render(request, 'auctions\signup.html')
    

'''
BID PRICE -> Rupesh
Search ->Rupesh
Posted by ___XYZ___ user -> Sailesh
Contact -> Sailesh
'''
