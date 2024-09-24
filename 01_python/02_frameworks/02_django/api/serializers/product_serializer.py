# -*- coding: utf-8 -*-
from ..models.product import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    """
    Serializer for product
    """
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'max_discount_price'
        ]
