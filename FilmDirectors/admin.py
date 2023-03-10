from django.contrib import admin
from .models import Genre, Film, Director

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Film)
