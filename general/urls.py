from django.contrib import admin
from django.urls import path 
from general import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name = 'search'),
]
