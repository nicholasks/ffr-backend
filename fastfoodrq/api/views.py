from django.shortcuts import render
from rest_framework import viewsets
from fastfoodrq.api.serializers import (
    ProductSerializer,
    CategorySerializer,
    IngredientSerializer,
    TagSerializer,
)
from fastfoodrq.ordering.models import (
    Product,
    Category,
    Ingredient,
    Tag,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
