from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path 
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('signup/', views.signup, name='signup' ),
     path('login/', views.signin, name ='login'),
     path('logout', views.userlogout, name='logout'),
     path('reset-password/', auth_views.PasswordResetView.as_view(template_name="reset-password.html") , name="reset-password"),
     path('reset-details-sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset-details-sent.html") , name="password_reset_done"),
     path('new-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="new-password.html") , name="password_reset_confirm"),
     path('new-password-success/', auth_views.PasswordResetCompleteView.as_view(template_name="new-password-success.html") , name="password_reset_complete"),

]
