from django.db import models
from app.models.User import User


class Recipe(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    datetime_created = models.DateTimeField()
    datetime_updated = models.DateTimeField(auto_now=True)
    