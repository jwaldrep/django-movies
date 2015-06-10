import csv
import json

print("Converting users...")
users = []
with open("data/ml-1m/users.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        users.append({"model": "movies.Rater",
                      "pk": row[0],
                      "fields": {
                          "age": row[2],
                          "zip_code": row[4]
                      }})

with open("movieratings/fixtures/users.json", "w") as outfile:
    outfile.write(json.dumps(users))

print("Converting movies...")
movies = []
with open("data/ml-1m/movies.dat", encoding="windows-1252") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for row in reader:
        movies.append({"model": "movies.Movie",
                       "pk": row[0],
                       "fields": {
                           "title": row[1]
                       }})

with open("movieratings/fixtures/movies.json", "w") as outfile:
    outfile.write(json.dumps(movies))

print("Converting ratings...")
ratings = []
with open("data/ml-1m/ratings.dat") as infile:
    reader = csv.reader((line.replace("::", ";") for line in infile),
                        delimiter=";")
    for idx, row in enumerate(reader):
        ratings.append({"model": "movies.Rating",
                        "pk": idx + 1,
                        "fields": {
                            "rater": row[0],
                            "movie": row[1],
                            "rating": row[2]
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
