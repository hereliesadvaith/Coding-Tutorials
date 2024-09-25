# -*- coding: utf-8 -*-
from . import views
from django.urls import path


urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('product/', views.product, name='product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(),
        name='product_detail'     
    ),
    path('product/create/', views.ProductCreateView.as_view(),
        name='product_create'
    )
]
