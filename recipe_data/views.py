from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render,redirect, get_object_or_404



# Add Recipe
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user

            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})




# Recipe Detail
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    is_liked = False
    if recipe.upvotes.filter(id=request.user.id).exists(): 
        is_liked = True 
    
    is_unliked = False
    if recipe.downvotes.filter(id=request.user.id).exists(): 
        is_unliked = True     
        
    comments = recipe.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = CommentForm()    
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'comments': comments, 'form': form,         'is_liked':is_liked, 
        'total_upvotes': recipe.total_upvotes(), 'total_downvotes': recipe.total_downvotes(),})





def upvote(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_liked = False
    if recipe.upvotes.filter(id = request.user.id).exists():
        recipe.upvotes.remove(request.user)
        is_liked = False
    else:
        recipe.upvotes.add(request.user)
        is_liked = True

    context= {
        'is_liked':is_liked, 
        'total_upvotes': recipe.total_upvotes(),
        'recipe' : recipe,
    }  
    
    if request.is_ajax():
        html = render_to_string('upvote_section.html', context, request=request) 
        context = {'form': html}  
        return JsonResponse(context)



def downvote(request):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_unliked = False
    if recipe.downvotes.filter(id = request.user.id).exists():
        recipe.downvotes.remove(request.user)
        is_unliked = False
    else:
        recipe.downvotes.add(request.user)
        is_unliked = True

    context= {
        'is_unliked':is_unliked, 
        'total_downvotes': recipe.total_downvotes(),
        'recipe' : recipe,
    }  
    
    if request.is_ajax():
        html = render_to_string('downvote_section.html', context, request=request) 
        context = {'form': html}  
        return JsonResponse(context)







@login_required
def my_recipes(request):
    user = request.user
    recipes = Recipe.objects.filter(user=user)
    return render(request, 'my_recipes.html', {'recipes': recipes})