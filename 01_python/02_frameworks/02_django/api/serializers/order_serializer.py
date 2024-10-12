# -*- coding: utf-8 -*-
from ..models.order import Order
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    """
    Serializer for product
    """
    class Meta:
        model = Order
        fields = [
            'name',
        ]
