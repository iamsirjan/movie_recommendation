from django.contrib import admin
from .models import movie, genre, language, rating, user
# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'language', 'video')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'movie', 'user')


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'is_admin')


admin.site.register(language, LanguageAdmin)
admin.site.register(user, UserAdmin)

admin.site.register(movie, MovieAdmin)
admin.site.register(genre, GenreAdmin)
admin.site.register(rating, RatingAdmin)
