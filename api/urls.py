from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'wishlist', views.LikeViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
