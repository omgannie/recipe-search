from django.db import models
from app.models.Recipe import Recipe


class RecipeStep(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='steps')
    description = models.CharField(max_length=1000)
    datetime_created = models.DateTimeField()
    datetime_updated = models.DateTimeField(auto_now=True)
    