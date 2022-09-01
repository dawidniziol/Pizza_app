from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Ingredient(models.Model):

    name = models.CharField(max_length=255, unique=True)
    dough = models.BooleanField(blank=False)
    sauce = models.BooleanField(blank=False)
    pizza = models.BooleanField(blank=False)

    def __str__(self):
        return self.name

    @property
    def dough_bool(self):
        if self.dough:
            return "Yes"
        return "No"

    @property
    def sauce_bool(self):
        if self.sauce:
            return "Yes"
        return "No"

    @property
    def pizza_bool(self):
        if self.pizza:
            return "Yes"
        return "No"


class Recipe(models.Model):

    TYPE_CHOICES = (
        ("Pizza", "Pizza"),
        ("Sauce", "Sauce"),
        ("Dough", "Dough")
    )

    name = models.CharField(max_length=255)
    type = models.CharField(choices=TYPE_CHOICES, max_length=255)

    def __str__(self):
        return self.name




class RecipeIngredient(models.Model):

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.IntegerField()



