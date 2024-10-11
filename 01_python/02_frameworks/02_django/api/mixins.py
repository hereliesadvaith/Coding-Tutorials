# -*- coding: utf-8 -*-
from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class PermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
