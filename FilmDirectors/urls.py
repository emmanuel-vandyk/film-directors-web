from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('directors/', views.directors, name='directors'),
    path('films/', views.films, name='films'),
    path('genres/', views.genres, name='genres'),
    path('bio1/', views.bio1, name='bio1'),
    path('bio2/', views.bio2, name='bio2'),
    path('bio3/', views.bio3, name='bio3'),
    path('bio4/', views.bio4, name='bio4'),
    path('bio5/', views.bio5, name='bio5'),
    path('bio6/', views.bio6, name='bio6'),
    path('bio7/', views.bio7, name='bio7'),
    path('bio8/', views.bio8, name='bio8'),
    path('bio9/', views.bio9, name='bio9'),
]