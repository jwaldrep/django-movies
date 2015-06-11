from django.db.models import Count
from django.shortcuts import render
from .models import Rating, Movie, Rater
from django.contrib.auth.models import User


def index(request):
    movies = Rating.top_rated(20)
    # statuses = Status.objects.annotate(Count('favorite')).order_by('-posted_at')
    return render(request,
                  "pymdb/index.html",
                  {"movies": movies})

