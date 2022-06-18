from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World! </h1>")
    return render(request, 'auctions/index.html')
