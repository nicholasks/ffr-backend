from django.test import TestCase
from .models import Order, OrderItem, Product, Tab


class OrderingTestCase(TestCase):
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

    def test_order_item_refresh_total_price_with_default_quantity(self):
        """ OrderItem total price must be refreshed with default quantity """
        self.assertEqual(
            self.order_item.total_price,
            2.50,
            "Total price must be equal to product price with default quantity"
        )

    def test_order_item_refresh_total_price_with_more_units(self):
        """ OrderItem total price must be refreshed with no-default quantity"""
        order_item = self.order_item
        order_item.quantity = 4
        order_item.save()

        self.assertEqual(
            order_item.total_price,
            10.0,
            "Total price must be 4 times the unity price of the product"
        )

    def test_order_refresh_total_price_of_promo_product(self):
        """ OrderItem total price must be different with promotion product """
        order_item = self.order_item
        order_item.is_promo = True
        order_item.save()

        self.assertEqual(
            order_item.total_price,
            1.50,
            "Total price must consider if product are on promotion"
        )

    def test_order_total_refresh(self):
        """ Order total price must be refresh on OI added. """
        prod = Product.objects.create(name="bar", price=1.0)
        OrderItem.objects.create(
            product=prod,
            order=self.order,
        )

        self.assertEqual(
            self.order.total,
            3.5,
            "Total price of Order must be refreshed on new Order Items",
        )

    def test_tab_total_refresh(self):
        """ Tab total must be refreshed when order is saved """
        self.assertEqual(
            self.tab.total,
            2.50,
            "Tab total must be equal the sum of all orders"
        )
