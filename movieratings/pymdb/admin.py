from django.contrib import admin
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'occupation', 'zip_code']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rating_count', 'avg_rating', 'sorted_ratings', 'top_rated', 'release_date', 'genre', 'imbdb_url']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'movie', 'user', 'time']

# Register your models here.
admin.site.register(Rating, RatingAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
