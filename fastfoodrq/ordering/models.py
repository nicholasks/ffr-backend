from django.db import models


class Product(models.Model):
    """
    Describe and define a product, it can be a food or a drink.
    """
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        blank=True,
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
    )
    price = models.FloatField()
    price_promo = models.FloatField(
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='product/'
    )

    def __str__(self):
        return self.name


class Combo(models.Model):
    """
    A Combo is a set of products with a determined price and description
    """
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    products = models.ManyToManyField(
        'Product',
    )

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(
        max_length=32,
        unique=True,
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    REALIZADO = 'pe'
    RECEBIDO = 're'
    PRODUCAO = 'pr'
    ENTREGUE = 'en'
    STATUS_CHOICES = (
        (REALIZADO, 'Pedido realizado'),
        (RECEBIDO, 'Recebido'),
        (PRODUCAO, 'Em preparo'),
        (ENTREGUE, 'Entregue'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=REALIZADO,
    )
    items = models.ManyToManyField(
        Product,
        through='OrderItem',
        through_fields=('order', 'product'),
    )
    table = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )
    total = models.FloatField(
        null=True,
        blank=True,
    )


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    is_promo = models.BooleanField(
        default=False,
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
    )


class Tab(models.Model):
    """
    Define the Guest check tab (COMANDA)
    """
    qrCode = models.PositiveIntegerField(
        unique=True,
        blank=False,
    )
    orders = models.ManyToManyField(
        'Order',
        blank=True,
    )
    total = models.FloatField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.qrCode)
