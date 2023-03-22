from django import forms
from .models import Recipe, Comment
from django.template.defaultfilters import linebreaksbr


class MultiLineTextInput(forms.TextInput):
    def format_value(self, value):
        if value:
            value = value.replace('\n', '<br>')
        return super().format_value(value)


class RecipeForm(forms.ModelForm):

    recipe_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter recipe name'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'A list of all ingredients: \n1. Water \n2. Butter....'}))
    cooking_duration = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'I.e: 1hr, 2hrs, 20mins....'}))
    instructions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter instructions'}))
    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'placeholder': 'Select image(s)'}))
    instructions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'A step by step guide: \nStep 1: .... \nStep 2: .... '}))


    class Meta:
        model = Recipe
        fields = ['recipe_name', 'ingredients', 'cooking_duration', 'image', 'instructions']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
