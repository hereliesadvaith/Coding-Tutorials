# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    """
    Model for Orders
    """
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
