# -*- coding: utf-8 -*-
from ..models.product import Product
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from rest_framework.validators import UniqueValidator


class ProductSerializer(ModelSerializer):
    """
    Serializer for product
    """
    name = CharField(validators=[
        UniqueValidator(queryset=Product.objects.all())
    ])
    discounted_price = SerializerMethodField(read_only=True)
    url = SerializerMethodField(read_only=True)
    email = EmailField(write_only=True)
    # Can also use foreign key as source
    title = CharField(source='name', read_only=True)

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
            'title',
            'email',
            'price',
            'max_discount_price',
            'discounted_price',
        ]
    
    def create(self, validated_data):
        # Can send an email on create
        email = validated_data.pop('email')
        return super().create(validated_data)

    # def validate_name(self, value):
    #     product = Product.objects.filter(name__exact=value)
    #     if product.exists():
    #         raise ValidationError(f'Product {value} already exists')
    #     return value
