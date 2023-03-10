from django.shortcuts import render
from .models import Director, Film, Genre
from django.http import HttpResponse
from django.template import loader

def index(request):
    num_directors = Director.objects.all().count()
    num_films = Film.objects.all().count()
    num_genres = Genre.objects.all().count()

    return render(
        request,
        'index.html',
        context = {
            'num_directors': num_directors,
            'num_films': num_films,
            'num_genres': num_genres,
        }
    )


def directors(request):
    show_directors = Director.objects.all()
    
    return render(
        request,
        'directors.html',
        context = {'object_list': show_directors}
    )


def films(request):
    show_films = Film.objects.all()
    
    return render(
        request,
        'films.html',
        context = {'object_list': show_films}
    )

def genres(request):
    show_genres = Genre.objects.all()
    return render(
        request,
        'genres.html',
        context = {'object_list': show_genres}
    )

def bio1(request):
    biography = Director.objects.get(pk=1).biography
    filmography = Film.objects.values('id', 'filmName')
    template = loader.get_template('bio1.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio2(request):
    biography = Director.objects.get(pk=2).biography
    filmography = Film.objects.values('id', 'filmName')
    template = loader.get_template('bio2.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))
    

def bio3(request):
    biography = Director.objects.get(pk=3).biography
    filmography = Film.objects.values('id', 'filmName')
    template = loader.get_template('bio3.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio4(request):
    biography = Director.objects.get(pk=4).biography
    filmography = Film.objects.values('id','filmName')
    template = loader.get_template('bio4.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))
    

def bio5(request):
    biography = Director.objects.get(pk=5).biography
    filmography = Film.objects.values('id', 'filmName')
    template = loader.get_template('bio5.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio6(request):
    biography = Director.objects.get(pk=6).biography
    filmography = Film.objects.values('id','filmName')
    template = loader.get_template('bio6.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio7(request):
    biography = Director.objects.get(pk=7).biography
    filmography = Film.objects.values('id','filmName')
    template = loader.get_template('bio7.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio8(request):
    biography = Director.objects.get(pk=8).biography
    filmography = Film.objects.values('id','filmName')
    template = loader.get_template('bio8.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))

def bio9(request):
    biography = Director.objects.get(pk=9).biography
    filmography = Film.objects.values('id', 'filmName')
    template = loader.get_template('bio9.html')
    context = {
    'biography': biography,
    'filmography': filmography}

    return HttpResponse(template.render(context, request))