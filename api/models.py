from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from djmoney.models.fields import MoneyField


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=128)


class Product(models.Model):
    title = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    price = MoneyField(
        default=0, default_currency='USD', decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class TypeOfDelivery(models.Model):
    title = models.CharField(max_length=128)
    fee = MoneyField(
        default=0, default_currency='USD', decimal_places=2, max_digits=6)


class Order(models.Model):
    title = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    total_price = MoneyField(
        default=0, default_currency='USD', decimal_places=2, max_digits=6)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_of_delivery = models.ForeignKey(
        TypeOfDelivery, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(models.signals.pre_save, sender=Order)
def order_total_price_pre_save(sender, instance, raw, *args, **kwargs):
    products_price = instance.quantity * instance.product.price
    fee = instance.type_of_delivery.fee

    if str(fee.currency) == settings.PERCENT_CURRENCY:
        instance.total_price = products_price * (fee.amount + 100) / 100
    else:
        instance.total_price = products_price + fee
