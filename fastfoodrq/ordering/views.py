import django_tables2 as tables

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Order, OrderItem


class OrderItemTable(tables.Table):
    class Meta:
        model = OrderItem
        template_name = 'django_tables2/bootstrap.html'


def index(request):
    table = OrderItemTable(OrderItem.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'simple_list.html', {'orders': table})
