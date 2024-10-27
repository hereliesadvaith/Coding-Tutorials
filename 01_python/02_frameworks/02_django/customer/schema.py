# -*- coding: utf-8 -*-
from .models import Customer
from graphene import List, ObjectType, Schema
from graphene_django import DjangoObjectType


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'city'
        )


class Query(ObjectType):
    customers = List(CustomerType)

    def resolve_customers(self, info, **kwargs):
        return Customer.objects.all()

schema = Schema(query=Query)
