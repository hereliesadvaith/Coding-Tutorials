# -*- coding: utf-8 -*-
from ..models.order import Order
from rest_framework.reverse import reverse
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for product
    """
    class Meta:
        model = Order
        fields = [
            'name',
            'partner'
        ]
    
    partner = serializers.CharField(source='user.username', read_only=True)
