# -*- coding: utf-8 -*-
from .models.product import Product
from .serializers.product_serializer import ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
