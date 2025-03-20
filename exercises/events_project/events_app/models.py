from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_founded = models.PositiveIntegerField()
    number_of_performances = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event = models.CharField(max_length=100)

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    poster = models.ImageField(upload_to='events_photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    outdoor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"