# Generated by Django 4.1.2 on 2022-11-01 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmDirectors', '0002_alter_film_sinopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='films',
            field=models.ManyToManyField(to='FilmDirectors.film'),
        ),
    ]