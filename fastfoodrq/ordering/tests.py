from django.test import TestCase
from .models import Order, OrderItem, Product, Tab


class OrderItemTestCase(TestCase):
    def setUp(self):
        self.tab = Tab.objects.create(qrCode=12345)
        self.product = Product.objects.create(
            name="foo",
            price=2.50,
            price_promo=1.50,
        )
        self.order = Order.objects.create(tab=self.tab)
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
        )

    def test_refresh_total_price_with_default_quantity(self):
        """ OrderItem total price must be refreshed with default quantity """
        self.assertEqual(
            self.order_item.total_price,
            2.50,
            "Total price must be equal to product price with default quantity"
        )

    def test_refresh_total_price_with_more_units(self):
        """ OrderItem total price must be refreshed with no-default quantity"""
        order_item = self.order_item
        order_item.quantity = 4
        order_item.save()

        self.assertEqual(
            order_item.total_price,
            10.0,
            "Total price must be 4 times the unity price of the product"
        )

    def test_refresh_total_price_of_promo_product(self):
        """ OrderItem total price must be different with promotion product """
        order_item = self.order_item
        order_item.is_promo = True
        order_item.save()

        self.assertEqual(
            order_item.total_price,
            1.50,
            "Total price must consider if product are on promotion"
        )
