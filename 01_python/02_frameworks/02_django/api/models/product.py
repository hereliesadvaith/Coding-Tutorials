# -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    """
    Model for products
    """
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)

    @property
    def max_discount_price(self):
        """
        Get max discount price
        """
        return float('%.2f' %(float(self.price) * 0.75))
