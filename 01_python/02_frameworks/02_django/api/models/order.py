# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class OrderQuerySet(models.QuerySet):
    def search(self, query, user=None):
        lookup = models.Q(name__icontains=query)
        return self.filter(lookup)


class OrderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return OrderQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Order(models.Model):
    """
    Model for Orders
    """
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    objects = OrderManager()
