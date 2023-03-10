# Generated by Django 4.1.2 on 2022-11-01 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FilmDirectors', '0003_alter_director_films'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='films',
            field=models.ManyToManyField(default='', to='FilmDirectors.film'),
        ),
        migrations.AlterField(
            model_name='director',
            name='firstName',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='FilmDirectors.director'),
        ),
    ]
