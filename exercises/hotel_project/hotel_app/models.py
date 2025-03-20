from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    number_of_beds = models.PositiveIntegerField()
    has_balcony = models.BooleanField(default=False)
    cleaned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number}"

class Employee(models.Model):
    TYPE_CHOICES = [
        ("H", "Hygienist"),
        ("R", "Receptionist"),
        ("M", "Manager"),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    tasks_description = models.TextField()
    employment_year = models.PositiveIntegerField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    room = models.ManyToManyField(Room, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Reservation(models.Model):
    code = models.CharField(max_length=10, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_image = models.ImageField(upload_to="reservation_images/", null=True, blank=True)
    booking_confirmation = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room}"