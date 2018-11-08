from django.shortcuts import render
from rest_framework import viewsets, generics
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
