from django.contrib import admin
from django.urls import path
from TravelApp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.reg, name='contact'),
    path('elements',views.Register,name='elements'),
    path('destinations',views.Login,name='destinations'),
    path('news',views.loginView,name='news'),
    
]
