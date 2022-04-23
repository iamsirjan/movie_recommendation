# Generated by Django 4.0 on 2022-04-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_movie_genre_movie_genre_remove_movie_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_banner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='movieDuration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratedfor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='releasedAt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
