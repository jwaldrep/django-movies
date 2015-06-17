"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pymdb import views as pymdb_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),  # FIXME: Is this needed?
    url(r'^$', pymdb_views.index, name="index"),
    url(r'^rater/(?P<rater_id>\d+)$', pymdb_views.show_rater, name="show_rater"),
    url(r'^movie/(?P<movie_id>\d+)$', pymdb_views.show_movie, name="show_movie"),
    url(r'^register/$', pymdb_views.user_register, name="user_register"),
    url(r'^logout$', pymdb_views.logout_view, name="logout"),
    # url(r'rate/$', pymdb_views.rate, name="rate"),
    url(r'^genre/(?P<genre_id>\d+)$', pymdb_views.show_genre, name="show_genre"),
    url(r'^movies/$', pymdb_views.MovieListView.as_view(), name="show_movies"),
    url(r'^ratings.png', pymdb_views.ratings_chart, name="ratings_chart")
]
