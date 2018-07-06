from django.http import JsonResponse
from django.views import generic
from rest_framework import viewsets

from .serializers import LikeSerializer
from .serializers import OrderSerializer
from .serializers import ProductSerializer

from .models import Like
from .models import Order
from .models import Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    page_size = 1

    def get_queryset(self):
        title = self.request.GET.get('title', None)
        category = self.request.GET.get('category', None)

        products = Product.objects.all()

        if title:
            products = products.filter(title__contains=title)
        if category:
            products = products.filter(category__title__exact=category)

        return products


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    page_size = 1

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    page_size = 1


class OrderView(generic.CreateView):
    model = Order
    fields = [
        'title',
        'quantity',
        'product',
        'type_of_delivery'
    ]

    def get(self, request):
        return JsonResponse({'error': 'Not Implemented'}, status=405)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        form.instance.user = self.request.user

        return JsonResponse({'data': {'id': self.object.id}})
