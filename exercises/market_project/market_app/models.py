from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Contact(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.street} {self.street_number}"

class Market(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    number_of_markets = models.PositiveIntegerField()
    date_opened = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_time = models.TimeField()
    ending_time = models.TimeField()

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Product(models.Model):
    TYPE_CHOICES = [
        ("FOOD", "Food"),
        ("DRINK", "Drink"),
        ("BAKERY", "Bakery"),
        ("COSMETIC", "Cosmetic"),
        ("HYGIENIC", "Hygienic"),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    homemade = models.BooleanField(default=False)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} {self.type}"

class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.market.name} {self.product.name} {self.quantity}"