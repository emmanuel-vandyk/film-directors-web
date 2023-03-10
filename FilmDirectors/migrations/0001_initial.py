# Generated by Django 4.1.2 on 2022-11-01 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(help_text='Pone el nombre del género', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmName', models.CharField(help_text='Pon el nombre de la película', max_length=32)),
                ('releaseYear', models.DateField(blank=True, null=True)),
                ('sinopsis', models.TextField(default=False, help_text='Agrega una sinopsis de la película')),
                ('genre', models.ManyToManyField(to='FilmDirectors.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(help_text='Apellido del director', max_length=100)),
                ('biography', models.TextField(help_text='Agrega una breve biografía del/la director/a')),
                ('films', models.ManyToManyField(related_name='+', to='FilmDirectors.film')),
                ('firstName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FilmDirectors.director')),
            ],
        ),
    ]
