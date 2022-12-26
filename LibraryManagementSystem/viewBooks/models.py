from django.db import models

# Create your models here.
class Book(models.Model):
    isbn=models.PositiveIntegerField()
    title=models.TextField()
    publishYear=models.PositiveIntegerField()
    pages=models.PositiveIntegerField()
    author=models.TextField()
    status=models.TextField()
