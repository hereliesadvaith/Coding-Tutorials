# -*- coding: utf-8 -*-
from ..models.product import Product
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ProductSerializer(ModelSerializer):
    """
    Serializer for product
    """
    discounted_price = SerializerMethodField(read_only=True)

    def get_discounted_price(self, obj):
        """
        Return max discount
        """
        return float(obj.price) - obj.max_discount_price

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'max_discount_price',
            'discounted_price'
        ]
