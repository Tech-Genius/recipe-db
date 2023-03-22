from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect
from . models import *
from django.db.models import Q
from django.core.mail import send_mail
from recipe import settings 
from recipe_data.models import *
# Create your views here.


# HOME

def home(request):

    recipes = Recipe.objects.all()
    return render(request, 'index.html',  {'recipes' : recipes}) 




# search

def search(request):

    if request.method == 'GET':
        q = request.GET['q']
        results = Recipe.objects.filter(Q(recipe_name__icontains=q)).distinct()
        context = {'q': q, 'results': results}
        return render(request, 'search.html', context)
        
    else:
        return render(request, 'search.html', {}) 

