from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('peliculas', views.peliculas, name='Peliculas'),
    path('genres', views.genres, name='Genres'),
    path('directors', views.directors, name='Directors'),
    path('formHTML', views.form_hmtl),
    path('genre-django-forms', views.genre_forms_django, name='GenreDjangoForms'),
    path('pelicula-django-forms', views.pelicula_forms_django, name='PeliculaDjangoForms'),
    path('directors-django-forms', views.directors_forms_django, name='DirectorsDjangoForms'),
    path('search', views.search, name='Search'),
]
