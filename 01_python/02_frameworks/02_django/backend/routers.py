# -*- coding: utf-8 -*-
from api.viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, 'products')

urlpatterns = router.urls
print(urlpatterns)
