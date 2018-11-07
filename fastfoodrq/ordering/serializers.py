from rest_framework import serializers
from fastfoodrq.ordering.models import (
    Product,
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
        )
