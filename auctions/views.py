from pyexpat.errors import messages
from django.shortcuts import redirect, render, HttpResponse
from sympy import content
from .models import Product
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password2 = request.POST.get('password')

        user = authenticate(request, username=username, password=password2)
        if user is not None:
            login(request, user)
            fname = user.full_name
            return render(request,"auctions/index.html",{'full_name':fname})
        else:
            messages.error(request,"Bad credientials!")
            return redirect('auctions/index.html')
    
    return render(request, "auctions/login.html")


def items(request,title):
    return render(request, 'auctions/items.html',{'item':title})


def about(request):
    return render(request, 'auctions/about.html')


def contact(request):
    return render(request, 'auctions/contact.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request,"username already exist ! please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already regeistered !")
            return redirect("home")

        if len(username)>10:
            messages.error(request,"username must be ub=nder 10 character !")

        if password1 != password2 :
            messages.error(request, "password didn't match")

        

        myuser = User.objects.create_user(username, email,password1)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()

        messages.success(request, "Your account has been created successfully.")

        return redirect('auctions/login.html')


    return render(request, "auctions/signup.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('home')