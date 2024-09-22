# -*- coding: utf-8 -*-
from django.http import JsonResponse
from .models.product import Product


def api_home(request):
    """
    Return all the available endpoints.
    """
    return JsonResponse({
        'message': 'Welcome'
    })
