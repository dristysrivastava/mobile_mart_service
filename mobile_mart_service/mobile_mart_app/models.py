from django.db import models


class Mobile(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    colour = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.colour} {self.brand} {self.model}: ₹ {self.price}"
