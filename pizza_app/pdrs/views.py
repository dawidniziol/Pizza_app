
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

    # ingredient_dict={
    #     "Dough": [True, False, False],
    #     "Sauce": [False, True, False],
    #     "Pizza": [False, False, True],
    #
    # }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # ingredient_choice=form.cleaned_data["type"]
            # Recipe.objects.create(
            #     name=form.cleaned_data["name"],
            #     dough= ingredient_dict[ingredient_choice][0],
            #     sauce= ingredient_dict[ingredient_choice][1],
            #     pizza= ingredient_dict[ingredient_choice][2]
            # )

    data = {'form': form, 'Recipe_list': Recipe_list}
    return render(request, template_name, data)


def doughedit_details(request, id, template_name='DoughEdit.html'):

    Recipe = Recipe.object.get(id=id)


    data = {'form': form, 'doughedit': doughedit}
    return render(request, template_name, data)




