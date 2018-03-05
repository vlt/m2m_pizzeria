from django.db import models
from django.urls import reverse


class Pizza(models.Model):
    toppings = models.ManyToManyField(
        "Topping",
        through="ToppingOnPizza",
    )

    def __str__(self):
        return "{}: {}".format(self.pk, list(self.toppings.all()))

    def get_absolute_url(self):
        return reverse("pizza_update", args=[self.pk])


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return str(self)


class ToppingOnPizza(models.Model):
    pizza = models.ForeignKey(
        "Pizza",
        on_delete=models.CASCADE,
    )
    topping = models.ForeignKey(
        "Topping",
        on_delete=models.CASCADE,
    )
