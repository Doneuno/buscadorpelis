import datetime
from django import forms
from django.forms import ModelForm
from app_coder.models import Pelicula


class GenreForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Genero')
    movies = forms.CharField(max_length=200, min_length=3, label='Pelicula')


class PeliculaForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=3, label='Nombre')
    genre = forms.CharField(max_length=40, label='Genero')
    year = forms.IntegerField(label='Año')


class DirectorsForm(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    movies = forms.CharField(max_length=200)
    
