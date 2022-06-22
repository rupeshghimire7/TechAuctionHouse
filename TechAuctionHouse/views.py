from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

#create your views here:
def sign_up(request):
    fm=UserCreationForm()
    return render(request,'auctions/signup.html',{'form':fm})


