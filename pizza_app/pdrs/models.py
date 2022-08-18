from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    dough = models.BooleanField(blank=False, null=True)
    sauce = models.BooleanField(blank=False, null=True)
    pizza = models.BooleanField(blank=False, null=True)

    def __str__(self):
        return self.name


class DoughRecipe(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class IngredientDough(models.Model):

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True)
    weight = models.IntegerField()
    dough = models.ForeignKey(DoughRecipe, on_delete=models.CASCADE)


