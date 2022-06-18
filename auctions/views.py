from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World! </h1>")
    return render(request, 'auctions/index.html')


def login(request):
    return render(request, 'auctions/login.html')


def items(request):
    return render(request, 'auctions/items.html')


def about(request):
    return render(request, 'auctions/about.html')
