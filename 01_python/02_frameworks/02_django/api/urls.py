# -*- coding: utf-8 -*-
from . import views
from django.urls import path


urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('product/', views.product, name='product'),
]
