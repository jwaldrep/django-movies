from django.db.models import Count, Avg
from django.shortcuts import render
from .models import Rating, Movie, Rater
from django.contrib.auth.models import User


def index(request):
    # movies = Rating.top_rated(20)
    # movies = Movie.objects.values('id').annotate(rating_count=Count('rating')).order_by('-rating_count')[:20]
        #    Employer.objects.values('id').annotate(jobtitle_count=Count('jobtitle')).order_by('-jobtitle_count')[:5]
    movies = Movie.objects.annotate(Avg('rating__rating')).order_by('-rating__rating__avg')[:20]
    # statuses = Status.objects.annotate(Count('favorite')).order_by('-posted_at')
    return render(request,
                  "pymdb/index.html",
                  {"movies": movies})

def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = sorted(rater.my_ratings(), key=lambda x: x.rating, reverse=True)
    return render(request,
                  'pymdb/user.html',
                  {'rater': rater,
                   'ratings': ratings,
                   })

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = movie.sorted_ratings()
    ratings = movie.rating_set.all()
    num_ratings = movie.rating_count()
    return render(request,
                  'pymdb/movie.html',
                  {'movie': movie,
                   'ratings': ratings,
                   'num_ratings': num_ratings,

                   })
