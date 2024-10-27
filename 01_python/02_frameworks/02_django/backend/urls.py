# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v2/', include('backend.routers')),
    path('graphql/', GraphQLView.as_view(graphiql=True))
]
