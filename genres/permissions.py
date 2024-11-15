from rest_framework import permissions


class GenrePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
