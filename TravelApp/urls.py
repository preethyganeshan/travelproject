from django.contrib import admin
from django.urls import path
from TravelApp import views

urlpatterns = [
    path('',views.index,name='index'),
    
]
