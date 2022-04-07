from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.deletion import SET, SET_NULL


class Book(models.Model):
    author = models.ForeignKey(
        "Author", on_delete=SET_NULL, related_name="books", null=True
    )
    name = models.CharField(max_length=254, blank=False, null=False)
    categories = models.ManyToManyField("Category", related_name="books")
    release_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    isbn = models.CharField(max_length=13)
    created_by = models.ForeignKey(
        User, on_delete=SET_NULL, related_name="created_books", null=True
    )
    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=1.0, 
        choices=(
            (1.0, 1.0),
            (2.0, 2.0),
            (10.01, 10.01)
        ),
        validators=[MaxValueValidator(10.01)]
    )
    field=models.DecimalField(decimal_places=4, default=1, max_digits=1000)



class Author(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDERS = ((MALE, "MALE"), (FEMALE, "FEMALE"))

    gender = models.CharField(max_length=1, choices=GENDERS)
    firstname = models.CharField(max_length=254, blank=False, null=False)
    lastname = models.CharField(max_length=254, blank=False, null=False)


class Category(models.Model):
    name = models.CharField(max_length=254, blank=False, null=False)
