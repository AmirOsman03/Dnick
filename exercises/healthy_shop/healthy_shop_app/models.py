from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Sale(models.Model):
    sold_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sold_product} {self.date}"