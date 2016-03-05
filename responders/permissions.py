from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAccountAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                request.user and
                request.user.is_staff):
            return True
        return False
