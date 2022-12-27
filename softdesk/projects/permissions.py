"""
Permissions for different views.
"""
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from projects.models import Contributor


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
        """
        check if the user is a contributor of the project
        """

        if request.method in SAFE_METHODS:
            contributors = list(
                Contributor.objects.filter(projects=view.kwargs["project_pk"]).values(
                    "user_id"
                )
            )

            contributors_id = []
            for contributor in contributors:
                contributors_id.append(contributor["user_id"])
            return request.user.id in contributors_id
        return obj.author_user == request.user
