from django import forms
from .models import Ingredient, DoughRecipe, IngredientDough


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = '__all__'


class DoughRecipeForm(forms.ModelForm):

    class Meta:
        model = DoughRecipe
        fields = '__all__'


class IngredientDoughForm(forms.ModelForm):

    class Meta:
        model = IngredientDough
        fields = '__all__'

