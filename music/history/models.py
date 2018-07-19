from django.db import models

# Create your models here.

class Artist(models>Model):
    artist_name = models.Charfield(max_length=20)
    band_name = models.CharField(max_length=50)
    still_active = models.BooleanField

class Song(models>Model):
    song_name = models.CharField(max_length=20)
    song_length = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
