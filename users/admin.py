from django.contrib import admin
from .models import movie, genre, language, rating
# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'language', 'video')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'movie', 'user')


admin.site.register(language, LanguageAdmin)
admin.site.register(movie, MovieAdmin)
admin.site.register(genre, GenreAdmin)
admin.site.register(rating, RatingAdmin)
