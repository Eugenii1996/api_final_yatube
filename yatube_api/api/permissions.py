from rest_framework.permissions import (
    BasePermission, SAFE_METHODS)


class OwnerOrReadOnly(BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.author == request.user
