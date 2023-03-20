from django.urls import path
from recipe_data import views


urlpatterns = [
   path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
   path('add-recipe', views.add_recipe, name='add_recipe'),
   # path('delete-recipe/<int:pk>/', views.delete_recipe, name='delete-recipe'), 
]
