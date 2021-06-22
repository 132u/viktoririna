from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework import permissions

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['date', 'customer', 'price', 'driver_name']
    search_fields = ['date', 'customer', 'price', 'driver_name']
    ordering_fields = ['date', 'customer', 'price', 'driver_name']


