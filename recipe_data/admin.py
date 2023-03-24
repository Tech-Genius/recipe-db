from django.contrib import admin
from . models import *

# Register your models here.

def approve_recipe(modeladmin, request, queryset):
    queryset.update(is_approved=True)

def reject_recipe(modeladmin, request, queryset):
    queryset.update(is_approved=False)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_name', 'is_approved']
    actions = [approve_recipe, reject_recipe]




admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)