# -*- coding: utf-8 -*-
from .models.product import Product
from .serializers.product_serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_home(request):
    """
    Return all the available endpoints.
    """
    routes = {
        'endpoints': [
            {
                'endpoint': '/api/token/',
                'method': 'POST',
                'description': 'Obtain a new token by providing username and password.'
            },
        ],
        'status': 'operational',
    }
    return Response(routes)

@api_view(['GET'])
def product(request):
    """
    Return products
    """
    records = Product.objects.all()
    data = {}
    if records:
        data = ProductSerializer(records, many=True).data
    return Response(data)
