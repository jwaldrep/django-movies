from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Rating, Movie, Rater
from django.contrib.auth.models import User
from pymdb.forms import UserForm, RaterForm, RatingForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


# TODO: Possible features:
#   Most active users (add to index using bootstrap columns)
#       Both in terms of most ratings and most reviews
#   Suggested movies
#       |-> Correlation curve using Pandas with generated similar movies
#   +Jumbotron image (requires css)
#   Alternating colors on rows, maybe tables? What layout would look good?

# FIXME: Prevent multiple users from logging in simultaneously
def show_genre(request, genre_id):
    movies = Movie.objects.filter(genre=genre_id) \
                 .annotate(rating_avg=Avg('rating__rating')) \
                 .annotate(rating_count=Count('rating__rating')) \
                 .filter(rating_count__gte=10) \
                 .order_by('-rating_avg')[:20] # TODO: Add lt 10 movies separately
    genre = movies[0].genre
    return render(request,
                  "pymdb/genre.html",
                  {"movies": movies})


def index(request):
    # movies = Rating.top_rated(20)
    # movies = Movie.objects.values('id').annotate(rating_count=Count('rating')).order_by('-rating_count')[:20]
    #    Employer.objects.values('id').annotate(jobtitle_count=Count('jobtitle')).order_by('-jobtitle_count')[:5]
    movies = Movie.objects.annotate(rating_avg=Avg('rating__rating')).annotate(
        rating_count=Count('rating__rating')).filter(
        rating_count__gte=10).order_by('-rating_avg')[:10]
    most_rated = Movie.objects.annotate(
        rating_avg=Avg('rating__rating')).annotate(
        rating_count=Count('rating__rating')).order_by('-rating_count')[:10]
    # counts = movies.
    # Item.objects.annotate(type_count=models.Count("type")).filter(type_count__gt=1).order_by("-type_count")

    # statuses = Status.objects.annotate(Count('favorite')).order_by('-posted_at')
    return render(request,
                  "pymdb/index.html",
                  {"movies": movies,
                   "most_rated": most_rated,
                   })

class MovieListView(ListView):
    template_name = "pymdb/movie_list.html"
    model = Movie
    context_object_name = 'movies'
    queryset = Movie.objects.annotate(rating_avg=Avg('rating__rating')).annotate(
        rating_count=Count('rating__rating')).filter(
        rating_count__gte=10).order_by('-rating_avg')  # FIXME: How to speed up this query?
    paginate_by = 20
    header = "Top Rated Movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = self.header
        # if self.request.user.is_authenticated():
        #     favorites = self.request.user.favorited_updates.all()
        # else:
        #     favorites = []
        # context["favorites"] = favorites
        return context

def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    # ratings = sorted(rater.my_ratings(), key=lambda x: x.rating, reverse=True)
    ratings = Rating.objects.filter(rater=rater).order_by('-time_added').select_related()
    return render(request,
                  'pymdb/user.html',
                  {'rater': rater,
                   'ratings': ratings,
                   })


# FIXME: 'AnonymousUser' object has no attribute 'rater'
def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # ratings = movie.sorted_ratings()
    ratings = movie.rating_set.all().order_by('-time_added').select_related()
    num_ratings = movie.rating_count()

    # FIXME: Rewrite to use a single query instead of many
    try:
        rater = None
        rater = request.user.rater
        r = Rating.objects.get(rater=rater, movie=movie)
    except (ObjectDoesNotExist, AttributeError):
        r = None

    if request.method == "GET":
        if r:
            rating_form = RatingForm(instance=r)
        else:
            rating_form = RatingForm()
    elif request.method == "POST":
        if r:
            rating_form = RatingForm(request.POST, instance=r)
        else:
            rating_form = RatingForm(request.POST)
        # rating_form.rater = rater  # Can't do this until after an uncommitted save...
        # rating_form.movie = movie
        if rating_form.is_valid() and not request.user.is_anonymous():
            # FIXME: Add error message for anon user trying to rate
            rating = rating_form.save(commit=False)
            rating.rater = rater
            rating.movie = movie
            # rating.save()
            # debug = [(x, getattr(rating_form, x)) for x in dir(rating_form)[65:]] #strike 4,65 >65 ok
            # debug2 = (dir(rating_form)[4], dir(rating_form)[65])
            # bug = 1/0
            rating_form.save()
            messages.add_message(request, messages.SUCCESS,
             "Your rating has been saved. Thank you for contributing!")


    return render(request,
                  'pymdb/movie.html',
                  {'movie': movie,
                   'ratings': ratings,
                   'num_ratings': num_ratings,
                   'rating_form': rating_form,
                   })


def user_register(request):
    if request.method == "GET":
        user_form = UserForm()
        rater_form = RaterForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)
        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            rater = rater_form.save(commit=False)
            rater.user = user
            rater.save()

            password = user.password
            # The form doesn't know to call this special method on user.
            user.set_password(password)
            user.save()

            # You must call authenticate before login. :(
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Congratulations, {}, on creating your new account! You are now logged in.".format(
                    user.username))
            return redirect('index')
    return render(request, "pymdb/register.html", {'user_form': user_form,
                                                   'rater_form': rater_form})


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
         "You have successfully logged out of PyMDb.")

    return redirect('index')

# def rate(request, movie_id, user):
#     if request.method == "GET":
#         rating_form = RatingForm()
#       # FIXME: Add redirect here? Does this ever run?
#     elif request.method == "POST":
#         r = Rating.objects.get(pk=1)
#         rating_form = RatingForm(request.POST, instance=r)
#         if rating_form.is_valid():
#             rating = rating_form.save(commit=False)
#             rating.save()
#             # rater.user = user
#             # rater.save()
#             #
#             # messages.add_message(
#             #     request,
#             #     messages.SUCCESS,
#             #     "Congratulations, {}, on creating your new account! You are now logged in.".format(
#             #         user.username))
#             # return redirect('index')
#     return render(request, "movie", {'rating_form': rating_form,   # FIXME: Add redirect
#                                      })
#     # return redirect('index')
