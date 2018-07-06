from django.contrib import admin

from .models import Category
from .models import Like
from .models import Order
from .models import Product
from .models import TypeOfDelivery


admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(TypeOfDelivery)
