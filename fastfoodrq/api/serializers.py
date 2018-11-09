from rest_framework import serializers
from fastfoodrq.ordering.models import (
    Product,
    Category,
    Ingredient,
    Tag,
    Tab,
    Order,
    OrderItem,
)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'category',
            'ingredients',
            'tags',
            'price',
            'price_promo',
            'image',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
            'parent',
        )


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('__all__')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'description')


class TabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tab
        fields = ('__all__')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')
