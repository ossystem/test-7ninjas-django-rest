import decimal

from django.test import TestCase
from djmoney.money import Money

from .models import Order
from .models import Product
from .models import TypeOfDelivery
from .models import order_total_price_pre_save


class OrderModelTests(TestCase):
    def test_delivery_price_percent_ok(self):
        product = Product(price=Money(100, 'USD'))
        type_of_delivery = TypeOfDelivery(fee=Money(10, 'PERCENT'))
        order = Order(
            type_of_delivery=type_of_delivery,
            product=product,
            quantity=10
        )

        order_total_price_pre_save(None, order, None)

        self.assertEqual(order.total_price.amount, 1100)

    def test_delivery_price_9_99_percent_ok(self):
        product = Product(price=Money(9.99, 'USD'))
        type_of_delivery = TypeOfDelivery(fee=Money(10, 'PERCENT'))
        order = Order(
            type_of_delivery=type_of_delivery,
            product=product,
            quantity=1
        )

        order_total_price_pre_save(None, order, None)

        self.assertAlmostEqual(
            order.total_price.amount, decimal.Decimal(10.989), places=2)

    def test_delivery_price_fixed_ok(self):
        product = Product(price=Money(100, 'USD'))
        type_of_delivery = TypeOfDelivery(fee=Money(10, 'USD'))
        order = Order(
            type_of_delivery=type_of_delivery,
            product=product,
            quantity=10
        )

        order_total_price_pre_save(None, order, None)

        self.assertEqual(order.total_price.amount, 1010)
