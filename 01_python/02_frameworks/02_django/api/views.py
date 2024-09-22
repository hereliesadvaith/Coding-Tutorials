"""
Views for routes.
"""
from django.http import JsonResponse


def api_home(request):
    """
    Return all the available endpoints.
    """
    return JsonResponse({
        'message': 'Welcome'
    })
