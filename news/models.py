"""Models File."""
from django.db import models

class Author(models.Model):
    """Author Model."""

    name = models.CharField(max_length=100)

class News(models.Model):
    """News Model."""

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    url = models.URLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
