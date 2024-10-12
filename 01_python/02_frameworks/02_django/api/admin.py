# -*- coding: utf-8 -*-
from .models.product import Product
from .models.order import Order
from django.contrib import admin


admin.site.register(Product)
admin.site.register(Order)
