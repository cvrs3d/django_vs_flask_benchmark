from datetime import datetime
# from itertools import product

from django.db import connection
# from rest_framework import viewsets
# from .serializers import OrderSerializer
from django.http import JsonResponse
from django.views import View
# from django.core import serializers
from .models import Order, Customer, Product

# class OrderViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
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
# class OrderView(View):
#     def get(self, request, pk):
#         with connection.cursor() as cursor:
#             cursor.execute("""
#             SELECT o.id, o.created_at, c.id, c.name, c.email, p.id, p.name, p.price
#             FROM testing_order as o
#             INNER JOIN testing_customer as c ON o.customer_id = c.id
#             INNER JOIN
#                 testing_order_products as op ON o.id = op.order_id
#             INNER JOIN testing_product as p ON op.product_id = p.id
#             WHERE o.id = %s
#             """, [pk])
#             rows = cursor.fetchall()
#
#             if rows:
#                 products = [
#                     {
#                         'id': row[5],
#                         'name': row[6],
#                         'price': row[7],
#                     } for row in rows
#                 ]
#                 data = {
#                     'order': {
#                         'id': rows[0][0],
#                         'created_at':
#                         datetime.strftime(rows[0][1], '%Y-%m-%d %H:%M:%S'),
#                         'customer': {
#                             'id': rows[0][2],
#                             'name': rows[0][3],
#                             'email': rows[0][4],
#                         },
#                         'products': products
#                     },
#                 }
#             else:
#                 data = {
#                     'error': 'Order not found',
#                 }
#             return JsonResponse(data)