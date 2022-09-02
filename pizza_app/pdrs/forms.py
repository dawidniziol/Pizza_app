from django import forms
from .models import Ingredient, Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

# DOUGH_CHOICES = (
#     ("Pizza", "Pizza"),
#     ("Sauce", "Sauce"),
#     ("Dough", "Dough")
# )
#
#
# class RecipeForm(forms.Form):
#
#     name = forms.CharField(label="Name")
#     type = forms.ChoiceField(label="Type", choices=DOUGH_CHOICES)


# class RecipeIngredientForm(forms.ModelForm):

    # class Meta:
    #     model = RecipeIngredient
    #     fields = '__all__'

class RecipeIngredientForm(forms.Form):

    ingredient = forms.ModelChoiceField(label="Ingredient", queryset=Ingredient.objects.all())
    weight = forms.IntegerField(label='weight')



