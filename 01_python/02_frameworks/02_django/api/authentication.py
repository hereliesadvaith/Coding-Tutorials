# -*- coding: utf-8 -*-
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'    
