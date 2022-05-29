from django.db import models


class Pelicula(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    year = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=40)
    movies = models.CharField(max_length=40)


class Director(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    movies = models.CharField(max_length=200)