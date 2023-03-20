
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']