from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World! </h1>")
    return render(request, 'auctions/index.html')


def login(request):
    return render(request, 'auctions/login.html')


def items(request,title):
    return render(request, 'auctions/items.html',{'item':title})


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    #return render(request, 'auctions/contact.html')
    return HttpResponse("<h1>CONTACT PAGE!</h1> <br> <h6>Remove # from render one and remove HttpResponse after contact.html page is done.!!!</h6>")
