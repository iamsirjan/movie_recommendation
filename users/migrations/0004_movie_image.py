# Generated by Django 4.0 on 2022-04-19 09:00

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_movie_actors_movie_description_movie_director_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.nameFile),
        ),
    ]
