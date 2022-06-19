from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'auctions/index.html')


def login(request):
    return render(request, 'auctions/login.html')


def items(request,title):
    return render(request, 'auctions/items.html',{'item':title})


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    return render(request, 'auctions/contact.html')
    