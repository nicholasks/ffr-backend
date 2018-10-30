from django.db import models


class Product(models.Model):
    """
    Describe and define a product, it can be a food or a drink.
    """

    name = models.CharField(
        max_lenght=32,
        unique=True,
        null=False,
    )
    description = models.CharField(
        max_lenght=128,
        null=True,
        blank=True,
    )
