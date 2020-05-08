from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
"""
Author model:

Name (CharField)
Bio (TextField)


Recipe Model:

Title (CharField)
Author link (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instruction = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
