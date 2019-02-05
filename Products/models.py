from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=1000000)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
