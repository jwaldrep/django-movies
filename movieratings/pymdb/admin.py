from django.contrib import admin
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'avg_rating', 'my_ratings', 'my_movies', 'ratings_vector', 'euclidean_distance', 'top_unseen', 'age', 'gender', 'occupation', 'zip_code']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rating_count', 'avg_rating', 'sorted_ratings']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'movie', 'rater', 'top_rated']

# Register your models here.
admin.site.register(Rating)#, RatingAdmin)
admin.site.register(Rater)#, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
