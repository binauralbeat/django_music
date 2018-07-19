from django.db import models

# Create your models here.

class Artist(models>Model):
    artist_name = models.Charfield(max_length=20)
    band_name = models.CharField(max_length=50)
    still_active = models.BooleanField
