from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Genre(models.Model):
    genre_name = models.CharField(max_length=64, unique=True)


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    summary = models.CharField(max_length=2048)
    reading_date = models.DateField()
