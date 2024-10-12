# -*- coding: utf-8 -*-
from ..models.product import Product
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer, SerializerMethodField, EmailField


class ProductSerializer(ModelSerializer):
    """
    Serializer for product
    """
    discounted_price = SerializerMethodField(read_only=True)
    url = SerializerMethodField(read_only=True)
    email = EmailField(write_only=True)

    def get_discounted_price(self, obj):
        """
        Return max discount
        """
        if not isinstance(obj, Product):
            return None
        return float(obj.price) - obj.max_discount_price
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request:
            return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
        return None

    class Meta:
        model = Product
        fields = [
            'url',
            'name',
            'email',
            'price',
            'max_discount_price',
            'discounted_price',
        ]
    
    def create(self, validated_data):
        # Can send an email on create
        email = validated_data.pop('email')
        return super().create(validated_data)

    def validate_price(self, value):
        # Check the value is valid or not before save
        return value
