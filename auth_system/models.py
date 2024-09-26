from django.db import models
from django.contrib.auth.models import AbstractUser
from shop.models import Product, Order

class CustomUser(AbstractUser):
    basket = models.ManyToManyField(Product, blank=True)
    orders = models.ManyToManyField(Order, blank=True)

    def __str__(self) -> str:
        return self.username
