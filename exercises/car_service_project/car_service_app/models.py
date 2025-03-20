from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    official_website = models.URLField()
    country = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Car(models.Model):
    TYPE_CHOICES = [
        ("SUV", "SUV"),
        ("SEDAN", "SEDAN"),
        ("HATCHBACK", "HATCHBACK"),
        ("COUPE", "COUPE"),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.PositiveIntegerField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} - {self.type}"

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.PositiveIntegerField()
    old_timer = models.BooleanField()
    manufacturer = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return f"{self.name}"

class Service(models.Model):
    code = models.CharField(max_length=10, unique=True)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.date}"