from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    본인의 매물장/매수장 접근 가능
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
