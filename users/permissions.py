from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
     Проверка пользователя - модератор или нет.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модератор").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверка пользователя - владелец или нет.
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
