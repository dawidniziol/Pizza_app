from django.db import models

# Create your models here.


class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    ingredient_dough = models.BooleanField(blank=True, null=True)
    ingredient_sauce = models.BooleanField(blank=True, null=True)
    ingredient_pizza = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name


class DoughRecipe(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class IngredientDough(models.Model):

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank= True)
    weight = models.IntegerField()
    dough = models.ForeignKey(DoughRecipe, on_delete=models.CASCADE)


