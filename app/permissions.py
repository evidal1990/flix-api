from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            request.method, view)
        if not model_permission_codename:
            return False
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            metadata = view.queryset.model._meta
            app_label = metadata.app_label
            action = self.__get_user_action(method)
            model_name = metadata.model_name
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def __get_user_action(self, method):
        method_actions = {
            "GET": "view",
            "OPTION": "view",
            "HEAD": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
        }
        return method_actions.get(method, "")
