from django.contrib import admin

# Register your models here.
from .models import Ingredient, DoughRecipe, IngredientDough

admin.site.register(Ingredient)
admin.site.register(DoughRecipe)
admin.site.register(IngredientDough)
