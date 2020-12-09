from django.db import models

class dataset(models.Model):
    gender = models.BooleanField()
    age = models.IntegerField
    salary = models.TextField()
    hobbies = models.TextField()
    in_extrovert = models.BooleanField()
    music_genre = models.TextField()
    movie_genre = models.TextField()
    gift = models.TextField()

