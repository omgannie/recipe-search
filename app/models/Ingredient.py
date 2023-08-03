from django.db import models
from app.models.Recipe import Recipe


class Ingredient(models.Model):
    used_in_recipes = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=10, null=True, default=None)
    