# -*- coding: utf-8 -*-
from .models.product import Product
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
