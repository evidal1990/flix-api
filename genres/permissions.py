from rest_framework import permissions


class GenrePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm("genres.view_genre")
        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")
        if request.method == "PUT":
				return request.user.has_perm("genres.change_genre")
		  if request.method == "DELETE":
				return request.user.has_perm("genres.delete_genre")
        return False