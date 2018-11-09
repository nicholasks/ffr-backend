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


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('__all__')


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('__all__')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    category = CategorySerializer(many=False, read_only=True)
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ('__all__')


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
