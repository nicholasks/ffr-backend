from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from fastfoodrq.api.serializers import ProductSerializer
from fastfoodrq.ordering.models import (
    Product,
)


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the ordering index.")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
