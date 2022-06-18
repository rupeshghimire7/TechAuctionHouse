from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('greet/<title>', views.greet, name='greet'),
    path('item',views.item, name='item')
]