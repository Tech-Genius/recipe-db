from django.db import models
# Create your models here.
from django.contrib.auth.models import User



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    cooking_duration = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    # slug = models.SlugField(default='', unique_for_date='date', blank=True)


    class Meta:
        ordering = ['-date_added']
        

    def __str__(self):
        return str(self.recipe_name)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=600)
    date_added = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-date_added'] 


    def __str__(self):
        return str(self.date_added)    
          


