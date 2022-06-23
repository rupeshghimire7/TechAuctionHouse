from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('items/<title>',views.items, name='items'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.signup, name='signup')
]
