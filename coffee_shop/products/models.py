import datetime
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponibilidad")
    photo = models.ImageField(
        default="/A_small_cup_of_coffee.JPG", blank=True, verbose_name="foto"
    )
    create = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
