from rest_framework import permissions


class ActorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm("actors.view_actor")
        if request.method == "POST":
            return request.user.has_perm("actors.add_actor")
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("actors.change_actor")
        if request.method == "DELETE":
            return request.user.has_perm("actors.delete_actor")
        return False
