from django.db import models
from django.urls import reverse

class Genre(models.Model):
    genreName = models.CharField(max_length=64, help_text="Pone el nombre del género")

    def __str__(self):
        return self.genreName

    def get_absolute_url(self):
        return reverse('genres', args=[str(self.id)])

class Film(models.Model):
    filmName = models.CharField(max_length=100, help_text="Pon el nombre de la película")
    genre = models.ManyToManyField(Genre, help_text="Agrega un género")
    releaseYear = models.DateField(null=True, blank=True)
    sinopsis = models.TextField(default="", help_text="Agrega una sinopsis de la película")

    def get_absolute_url(self):
        return reverse('films', args=[str(self.id)])
    
    def __str__(self):
        return self.filmName


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100, help_text="Nombre del director")
    lastName = models.CharField(max_length=100, help_text="Apellido del director")
    biography = models.TextField(help_text="Agrega una breve biografía del/la director/a")
    films = models.ManyToManyField(Film, default="")


    def get_absolute_url(self):
        return reverse('directors', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)