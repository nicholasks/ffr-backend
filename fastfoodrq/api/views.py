from django.shortcuts import render
from rest_framework import viewsets
from fastfoodrq.api.serializers import (
    ProductSerializer,
    CategorySerializer,
    IngredientSerializer,
    TagSerializer,
    TabSerializer,
    OrderSerializer,
    OrderItemSerializer,
)
from fastfoodrq.ordering.models import (
    Product,
    Category,
    Ingredient,
    Tag,
    Tab,
    Order,
    OrderItem,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TabViewSet(viewsets.ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer

    def get_queryset(self):
        queryset = self.queryset
        qrCode = self.request.query_params.get('qrCode', None)
        total = self.request.query_params.get('total', None)
        if qrCode is not None:
            queryset = queryset.filter(qrCode=qrCode)
            if total is not None:
                pass

        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
