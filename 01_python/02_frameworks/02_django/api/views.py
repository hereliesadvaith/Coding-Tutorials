# -*- coding: utf-8 -*-
from .mixins import PermissionMixin
from .models.order import Order
from .models.product import Product
from .permissions import IsStaffEditorPermission
from .serializers.order_serializer import OrderSerializer
from .serializers.product_serializer import ProductSerializer
from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


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

@api_view(['GET', 'POST'])
def product(request):
    """
    Return products
    """
    match request.method:
        case 'GET':
            records = Product.objects.all()
            data = {}
            if records:
                data = ProductSerializer(records, many=True).data
            return Response(data)
        case 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)


class ProductDetailView(generics.RetrieveAPIView):
    """
    Class for single product view get
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """
    Create product post method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        To extend create function
        """
        # serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class ProductListView(generics.ListAPIView):
    """
    Class for list of products view
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateView(
        PermissionMixin, generics.ListCreateAPIView
    ):
    """
    Both list and create combined
    GET method for list view
    POST method for create
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET method to retrieve one specific product data
    PUT method to update values
    DELETE method to delete the product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ProductCreateListMixins(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductRetrieveMixins(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OrderViewSet(
        PermissionMixin, viewsets.ModelViewSet
    ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs.filter(user=self.request.user)
        query = self.request.GET.get('query')
        result = qs.search(query=query, user=self.request.user)
        return result
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
