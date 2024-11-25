from itertools import product

from rest_framework import viewsets
from .serializers import OrderSerializer
from django.http import JsonResponse
from django.views import View
from django.core import serializers
from .models import Order, Customer, Product

# class OrderViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderView(View):
    def get(self, request, pk):
        order = Order.objects.select_related(
            'customer'
        ).prefetch_related('products').get(id=pk)

        data = {
            'order': {
                'id': order.id,
                'created_at': order.created_at,
                'customer': {
                    'id': order.customer.id,
                    'name': order.customer.name,
                    'email': order.customer.email,
                },
                'products': [
                    {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                    } for product in order.products.all()
                ]
            },
        }

        return JsonResponse(data)