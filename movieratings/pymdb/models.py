from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Schema Planning:
    u.data:
    user id | item id | rating | timestamp.
    196	242	3	881250949


    u.item:
     movie id | movie title | release date | video release date |
                  IMDb URL | unknown | Action | Adventure | Animation |
                  Children's | Comedy | Crime | Documentary | Drama | Fantasy |
                  Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
                  Thriller | War | Western |
    1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/
    title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0

    u.user:
    user id | age | gender | occupation | zip code
    1|24|M|technician|85711

    Rater: (id), fk(User), XXfk(movie)XX, XXfk(rating)XX, XXfk(timestamp)XX
        age, gender, occupation, zip_code

    Movie: (id), title, release_date, video_date, imdb_url, genre(0-18)

    Rating: (id), fk(Rater), fk(movie), rating, timestamp
"""
class Rater(models.Model):
    # user = models.ForeignKey(User)  # No, don't use this
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=64)
    zip_code = models.PositiveIntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    video_date = models.DateField()
    imbdb_url = models.URLField()
    genre = models.PositiveSmallIntegerField()

class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()
    time = models.DateTimeField()

