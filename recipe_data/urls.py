from django.urls import path
from recipe_data import views


urlpatterns = [
   path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
   path('add-recipe', views.add_recipe, name='add_recipe'),
   path('my-recipes', views.my_recipes, name='my_recipes'),
   path(r'^like/$', views.upvote, name='upvote'),
   path(r'^unlike/$', views.downvote, name='downvote'),
   # path('delete-recipe/<int:pk>/', views.delete_recipe, name='delete-recipe'), 
]
