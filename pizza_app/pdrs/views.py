
from .models import Ingredient, Recipe, RecipeIngredient
from django.shortcuts import render
from .forms import IngredientForm, RecipeForm, RecipeIngredientForm


def home_page(request, template_name='pdrs/home.html'):

    return render(request, template_name)


def ingredient_list(request, template_name='pdrs/IngredientViews.html'):

    form = IngredientForm(request.POST or None, initial={
        'dough': False,
        'sauce': False,
        'pizza': False
    })

    ingredient_list = Ingredient.objects.all()

    if form.is_valid():
        form.save()

    data = {'form': form, 'ingredient_list': ingredient_list}
    return render(request, template_name, data)


def Recipe_list(request, template_name='pdrs/Recipe.html'):

    form = RecipeForm(request.POST or None)

    Recipe_list = Recipe.objects.all()

    dough_list = Recipe.objects.filter(type="Dough")
    sauce_list = Recipe.objects.filter(type="Sauce")

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    data = {'form': form, 'Recipe_list': Recipe_list, 'dough_list': dough_list, 'sauce_list': sauce_list}
    return render(request, template_name, data)


def recipe_edit_details(request, id, template_name='pdrs/RecipeEdit.html'):

    form = RecipeIngredientForm(request.POST or None)
    recipe = Recipe.objects.get(id=id)
    recipe_ingredient = recipe.recipeingredient_set.all()

    if recipe.type == 'Dough':
        form.fields['ingredient'].queryset = Ingredient.objects.filter(dough=True)
    if recipe.type == 'Sauce':
        form.fields['ingredient'].queryset = Ingredient.objects.filter(sauce=True)

    # ing_dict = {'Dough': Ingredient.objects.filter(dough=True),
    #             'Sauce': Ingredient.objects.filter(sauce=True)}
    #
    # form.fields['ingredient'].queryset = ing_dict[recipe.type]

    if request.method == 'POST':
        if form.is_valid():
            RecipeIngredient.objects.create(
                ingredient=form.cleaned_data['ingredient'],
                recipe=recipe,
                weight=form.cleaned_data['weight']
            )

    data = {'form': form, 'recipe': recipe, 'recipe_ingredient': recipe_ingredient}
    return render(request, template_name, data)




