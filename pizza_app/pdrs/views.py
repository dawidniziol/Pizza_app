
from .models import Ingredient
from django.shortcuts import render
from .forms import IngredientForm


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


def home_page(request, template_name='pdrs/home.html'):

    return render(request, template_name)

