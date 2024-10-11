# -*- coding: utf-8 -*-
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth/', obtain_auth_token, name='obtain_auth_token'),
    path('', views.api_home, name='api_home'),
    # path('product/', views.product, name='product'),
    # path('product/<int:pk>/', views.ProductDetailView.as_view(),
    #     name='product_detail'     
    # ),
    path('product/create/', views.ProductCreateView.as_view(),
        name='product_create'
    ),
    path('product/list/', views.ProductListView.as_view(),
        name='product_list'
    ),
    path('product/', views.ProductListCreateView.as_view(),
        name='product_list_create'
    ),
    path('product/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(),
        name='product_retrieve_update_destroy'     
    ),
    path('product/mixin/', views.ProductCreateListMixins.as_view(),
        name='product_create_list_mixin'
    ),
    path('product/mixin/<int:pk>/', views.ProductRetrieveMixins.as_view(),
         name='product_retrieve_mixin'
    )
]
