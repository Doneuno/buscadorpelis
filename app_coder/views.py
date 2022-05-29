from django.shortcuts import render
from django.db.models import Q

from app_coder.models import Genre, Director, Pelicula
from app_coder.forms import GenreForm, PeliculaForm, DirectorsForm


def index(request):
    return render(request, "app_coder/home.html")


def peliculas(request):
    peliculas = Pelicula.objects.all()

    context_dict = {
        'peliculas': peliculas
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/peliculas.html"
    )


def genres(request):
    genres = Genre.objects.all()

    context_dict = {
        'genres': genres
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/genres.html"
    )


def directors(request):
    directors = Director.objects.all()

    context_dict = {
        'directors': directors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/directors.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        genre = Genre(name=request.POST['name'], code=request.POST['code'])
        genre.save()

        genres = Genre.objects.all()
        context_dict = {
            'genres': genres
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/genres.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def genre_forms_django(request):
    if request.method == 'POST':
        genre_form = GenreForm(request.POST)
        if genre_form.is_valid():
            data = genre_form.cleaned_data
            genre = Genre(name=data['name'], movies=data['movies'])
            genre.save()
            genres = Genre.objects.all()
            context_dict = {
                'genres': genres
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/genres.html"
            )

    genre_form = GenreForm(request.POST)
    context_dict = {
        'genre_form': genre_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/genre_django_forms.html'
    )


def directors_forms_django(request):
    if request.method == 'POST':
        director_form = DirectorsForm(request.POST)
        if director_form.is_valid():
            data = director_form.cleaned_data
            director = Director(
                name=data['name'],
                last_name=data['last_name'],
                movies=data['movies'],
            )
            director.save()

            directors = Director.objects.all()
            context_dict = {
                'director': directors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/directors.html"
            )

    director_form = DirectorsForm(request.POST)
    context_dict = {
        'pelicula_form': director_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/pelicula_django_forms.html'
    )
    
    
def pelicula_forms_django(request):
    if request.method == 'POST':
        pelicula_form = PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            data = pelicula_form.cleaned_data
            pelicula = Pelicula(
                name=data['name'],
                genre=data['genre'],
                year=data['year'],
            )
            pelicula.save()

            peliculas = Pelicula.objects.all()
            context_dict = {
                'peliculas': peliculas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/peliculas.html"
            )

    pelicula_form = PeliculaForm(request.POST)
    context_dict = {
        'pelicula_form': pelicula_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/pelicula_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['movie_search']:
        search_param = request.GET['movie_search']
        peliculas = Pelicula.objects.filter(name__contains=search_param)
        print(peliculas)
        context_dict = {
            'peliculas': peliculas
        }
    elif request.GET['genre_search']:
        search_param = request.GET['genre_search']
        genres = Genre.objects.filter(name__contains=search_param)
        print(genres)
        context_dict = {
            'genres': genres
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(genre__contains=search_param), Q.OR)
        print(query)
        peliculas = Pelicula.objects.filter(query)
        context_dict = {
            'peliculas': peliculas
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )
