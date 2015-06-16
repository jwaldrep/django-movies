from django.db import models
import math
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


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


def validate_movie_rating(value):
    if not 1 <= value <= 5:
        raise ValidationError("Rating must be between 1 and 5.")


class Genre(models.Model):
    # id = models.SmallIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

# FIXME: Ensure that new users are associated with a Rater
class Rater(models.Model):
    # rater = models.ForeignKey(User)  # No, don't use this
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=255, null=True) # FIXME: Delete this field
    job = models.PositiveSmallIntegerField(null=True)
    zip_code = models.CharField(max_length=255)
    user = models.OneToOneField(User, null=True)

    def avg_rating(self):
        ratings = [r['rating'] for r in self.rating_set.values()]
        num = self.rating_set.count()
        if num <= 0:
            return 0
        return sum(ratings) / num

    def top_unseen(self, n=2):
        # all_movies = Movie.objects.all()
        # my_movies = self.my_movies()
        ratings = Rating.top_rated(n=None) # Sorted by rating
        # seen = self.rating_set
        # return unseen[:n]
        return [r.movie for r in ratings if r.movie not in self.my_movies()]

    def my_ratings(self):
        return Rating.objects.filter(rater=self.id)

    def my_movies(self):
        return [r.movie for r in self.my_ratings()]

    def ratings_vector(self):
        movies = Movie.objects.all().order_by('pk')
        vector = [0 for m in movies]
        for i in range(len(vector)):
            if movies[i] in self.my_movies():
                vector[i] = self.my_ratings().filter(movie=movies[i])[0].rating
        return vector

    def euclidean_distance(self): #, other):
        other = self.__class__.objects.first()
        mine = self.ratings_vector()
        yours = other.ratings_vector()
        return math.sqrt(sum( (mine - yours)**2 for mine, yours in zip(mine, yours)))

    def __str__(self):
        return 'User #{}'.format(self.id)

    @classmethod
    def create_users_for_raters(cls):
        for rater in Rater.objects.all():
            user = User.objects.create(
                username='user' + str(rater.id).zfill(5),
                password='password',
                # ^^ This method won't work -- need to use set_password()!
                email=str(rater.id) + '@example.com',
            )
            user.set_password('password')
            user.save()
            rater.user = user
            rater.save()

    @classmethod
    def reset_all_passwords(cls):
        for rater in Rater.objects.all():
            u = rater.user
            print(u, "password reset to 'password'.")
            u.set_password('password')
            u.save()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    # release_date = models.DateField() # Removed for 1M database
    # video_date = models.DateField() # Removed for 1M database
    # imbdb_url = models.URLField()  # Removed for 1M database
    genre = models.ManyToManyField(Genre)

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
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField(validators=[validate_movie_rating])
    time_added = models.DateTimeField(default=timezone.now())
    time_modified = models.DateTimeField(default=timezone.now())

    @classmethod
    def top_rated(cls, n=2):
        ratings = sorted(cls.objects.all(), key=lambda x: x.rating, reverse=True)
        # ratings = [(r.id, r.rating) for r in rating_objs]
        return ratings[:n] if n else ratings

    @classmethod
    def set_modified_date_to_add_date(cls):
        for rating in Rating.objects.all():
            rating.time_modified = rating.time_added
            rating.save()

    def __str__(self):
        return '{} - {}'.format('*' * self.rating, self.movie.title)