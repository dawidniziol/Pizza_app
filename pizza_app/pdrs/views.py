
from .models import Ingredient, DoughRecipe, IngredientDough
from django.shortcuts import render
from .forms import IngredientForm, DoughRecipeForm, IngredientDoughForm


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


def doughrecipe_list(request, template_name='pdrs/DoughRecipe.html'):

    form = DoughRecipeForm(request.POST or None)

    doughrecipe_list = DoughRecipe.objects.all()

    if form.is_valid():
        form.save()

    data = {'form': form, 'doughrecipe_list': doughrecipe_list}
    return render(request, template_name, data)


def doughedit_details(request, id, template_name='DoughEdit.html'):

    id = DoughRecipe.object.get(id=pk)


    data = {'form': form, 'doughedit': doughedit}
    return render(request, template_name, data)




