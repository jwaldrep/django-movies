from django.contrib import admin
from .models import Movie, Rater, Rating

# Register your models here.
admin.site.register(Rating)
admin.site.register(Rater)
admin.site.register(Movie)
