from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        ##
        # TODO inserir a lógica de negócio da permissão
        # Abaixo, verifica-se via has_permission com a sintaxe padrão conforme abaixo
        ##
        if request.method in ("GET", "OPTIONS", "HEAD"):
            return request.user.has_perm("genres.view_genre")

        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")

        return False
