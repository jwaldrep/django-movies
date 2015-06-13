from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from .models import Rating, Movie, Rater
from django.contrib.auth.models import User
from pymdb.forms import UserForm, RaterForm, RatingForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# FIXME: Prevent multiple users from logging in simultaneously

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
    if request.method == "GET":
        rating_form = RatingForm()
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
    return redirect('index')


def rate(request):
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

