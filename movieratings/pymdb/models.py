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

    def avg_rating(self):
        ratings = [r['rating'] for r in self.rating_set.values()]
        num = self.rating_set.count()
        if num <= 0:
            return 0
        return sum(ratings) / num

    def top_unseen(self, n=2):
        pass

    def __str__(self):
        return 'User #{}'.format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    video_date = models.DateField()
    imbdb_url = models.URLField()  # TODO: Fix typo and migrate
    genre = models.PositiveSmallIntegerField()

    def rating_count(self):
        return self.rating_set.count()

    def sorted_ratings(self):
        rank_list = [(r['movie_id'], r['rating']) for r in self.rating_set.values()]
        return sorted(rank_list, key=lambda x: x[1], reverse=True)

    def avg_rating(self):
        ratings = [r['rating'] for r in self.rating_set.values()]
        num = self.rating_count()
        if num <= 0:
            return 0
        return sum(ratings) / num




    def __str__(self):
        return '{}'.format(self.title)

class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()
    time = models.DateTimeField()

    @classmethod
    def top_rated(cls, n=2):
        rating_objs = sorted(cls.objects.all(), key=lambda x: x.rating, reverse=True)
        ratings = [(r.id, r.rating) for r in rating_objs]
        return ratings[:n]

    def __str__(self):
        return '{} - {}'.format('*'*self.rating, self.movie.title)