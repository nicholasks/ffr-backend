import django_tables2 as tables

from django.db.models import Q
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Order, OrderItem


class OrderItemTable(tables.Table):
    class Meta:
        model = OrderItem
        template_name = 'django_tables2/bootstrap.html'
        exclude = ('is_promo', 'total_price', 'unity_price',)


def index(request):
    orders = Order.objects.all().filter(Q(status='pe') | Q(status='pr'))
    tb_orderItem = OrderItemTable(OrderItem.objects.all())
    tb_order = OrderTable(orders)

    RequestConfig(request).configure(tb_orderItem)
    return render(request, 'simple_list.html', {'order': tb_order, 'orderitem': tb_orderItem})


class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
