from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Order
from .models import Product
from .models import Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category = serializers.SlugRelatedField(read_only=True, slug_field='title')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['product']

    product = ProductSerializer()
