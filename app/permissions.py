from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        ##
        # TODO inserir a lógica de negócio da permissão
        # Abaixo, verifica-se via has_permission com a sintaxe padrão conforme abaixo
        ##
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, view=view
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            app_label = view.queryset.model._meta.app_label.lower()
            action = self.__get_action_suffix(method).lower()
            model_name = view.queryset.model._meta.model_name.lower()
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def __get_action_suffix(self, method):
        method_actions = {
            "HEAD": "view",
            "OPTIONS": "view",
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "DELETE": "delete",
        }

        return method_actions.get(method)
