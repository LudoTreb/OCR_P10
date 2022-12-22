from rest_framework import permissions


class IsProjectAuthor(permissions.BasePermission):
    """
    check if the user is the author of the project.
    """

    def has_object_permission(self, request, view, obj):
        if obj.author_user == request.user:
            return True
        return False


class IsProjectContributor(permissions.BasePermission):
    """
    check if the user is a contributor of the project
    """

    def has_object_permission(self, request, view, obj):
        pass
