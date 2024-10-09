# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    """
    Custom permission
    """
    # def has_permission(self, request, view):
    #     if request.user.is_staff:
    #         if request.method == 'GET':
    #             return request.user.has_perm('api.view_product')
    #     return super().has_permission(request, view)
    def __init__(self) -> None:
        super().__init__()
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
