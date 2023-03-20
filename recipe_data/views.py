from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm




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
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'comments': comments, 'form': form})
