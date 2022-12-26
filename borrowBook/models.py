from django.db import models

# Create your models here.
class Borrower(models.Model):
    student_id=models.PositiveIntegerField()
    name=models.TextField()
    email=models.TextField()
    phone=models.PositiveIntegerField()
    borrow_date=models.TextField()
    return_date=models.TextField()
    isbn=models.PositiveIntegerField()
    title=models.TextField()
