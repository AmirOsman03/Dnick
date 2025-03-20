from tkinter.tix import Balloon

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pilot(models.Model):
    RANK_CHOICES = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior"),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    flight_hours = models.IntegerField()
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=100)
    max_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer}"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    outside_Europe = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code = models.CharField(max_length=10, unique=True)
    take_off_airport = models.CharField(max_length=100)
    land_off_airport = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flight_images/', null=True, blank=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.take_off_airport} -> {self.land_off_airport}"