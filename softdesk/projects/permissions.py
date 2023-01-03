"""
Permissions for different views.
"""
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from projects.models import Contributor, Project


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

        return obj.contributor_set.filter(user_id=request.user).exists()


class IsIssueProjectContributor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.project.contributor_set.filter(user_id=request.user).exists()
