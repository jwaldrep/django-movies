import csv
import json
import datetime

print("Converting users...")
users = []
with open("data/ml-1m/users.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        users.append({"model": "pymdb.Rater",
                      "pk": row[0],
                      "fields": {
                          "gender": row[1],
                          "age": row[2],
                          "occupation": row[3],
                          "zip_code": row[4],
                      }})

with open("movieratings/fixtures/users.json", "w") as outfile:
    outfile.write(json.dumps(users))

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Children's",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western"]

genre_dict = dict(zip(genres, range(20)))

print("Converting genres...")
genres = []
for genre in genres:
    genres.append({"model": "pymdb.Genre",
                   "pk": genre_dict[genre],
                   "fields": {
                       # "id": genre_dict[genre],
                       "name": genre,
                   }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
    outfile.write(json.dumps(genres))


print("Converting movies...")
movies = []
with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
    reader = csv.reader((line.replace("::", "_") for line in infile),
                        delimiter="_")
    for row in reader:
        # print('0:', row[0], '1:', row[1], '2:', row[2])
        movies.append({"model": "pymdb.Movie",
                       "pk": row[0],
                       # "fields": {
                       #     "title": row[1],
                           "genre": [genre_dict[genre] for genre in row[2].split('|')],
                       }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
    outfile.write(json.dumps(movies))

print("Converting ratings...")
ratings = []
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for idx, row in enumerate(reader):
        ratings.append({"model": "pymdb.Rating",
                        "pk": idx + 1,
                        "fields": {
                            "rater": row[0],
                            "movie": row[1],
                            "rating": row[2],
                             #"time": row[3],
                            "time": str(datetime.datetime.fromtimestamp(int(row[3])))
                        }})

with open("movieratings/fixtures/ratings.json", "w") as outfile:
    outfile.write(json.dumps(ratings))


# print("Converting movies...")
# with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
#     reader = csv.reader((line.replace("::", ";") for line in infile),
#                         delimiter=";")
#     with open("data/ml-1m/movies.csv", "w", newline="") as outfile:
#         writer = csv.writer(outfile)
#         for row in reader:
#             writer.writerow(row[0:2])
#
# print("Converting ratings...")
# with open("data/ml-1m/ratings.dat") as infile:
#     reader = csv.reader((line.replace("::", ";") for line in infile),
#                         delimiter=";")
#     with open("data/ml-1m/ratings.csv", "w", newline="") as outfile:
#         writer = csv.writer(outfile)
#         for row in reader:
#             writer.writerow(row)
