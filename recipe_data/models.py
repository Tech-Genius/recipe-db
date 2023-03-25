from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    cooking_duration = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True, default='recipe_images/default_recipe_image.png')
    is_approved = models.BooleanField(default=None, null=True)
    # slug = models.SlugField(default='', unique_for_date='date', blank=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True, default=[0])
    downvotes = models.ManyToManyField(User, related_name='downvotes', blank=True, default=[0])


    def save(self, *args, **kwargs):
        # Check if an image is present
        if not self.image:
            # If no image is present, set the default image
            with open(os.path.join(settings.STATIC_ROOT, 'recipe_images/default_recipe_image.png'), 'rb') as f:
                self.image.save('default_recipe_image.png', File(f), save=False)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_added']
        

    def __str__(self):
        return str(self.recipe_name)


    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=600)
    date_added = models.DateTimeField(auto_now_add=True)





    class Meta:
        ordering = ['-date_added'] 


    def __str__(self):
        return str(self.content)    
          