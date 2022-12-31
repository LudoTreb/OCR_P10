"""
Views for project, issue, comment & contributor.
"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment, Contributor
from projects.permissions import IsProjectAuthor, IsProjectContributor
from projects.serializers import (
    ProjectSerializer,
    IssuesSerializer,
    CommentSerializer,
    ContributorSerializer,
)


class ProjectViewset(ModelViewSet):
    """
    This view allows all CRUD actions but only
    with some permissions.
    The create action is override
    to add contributors fields.
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        """
        Get a query set of all project.
        """

        return Project.objects.filter(author_user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        overide create action to fill the author_user field.
        """

        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class IssuesViewset(ModelViewSet):
    """
    This view allows all CRUD actions but only
    with some permissions.
    Some actions are overide to fill automaticaly some fields.
    """

    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        """
        Get a query set of all issues.
        """
        return Issue.objects.all()

    def create(self, request, project_pk=None, *args, **kwargs):
        """
        overide create action to fill the author_user and project fields.
        """
        project = get_object_or_404(Project, pk=project_pk)
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        request_data["project"] = project_pk
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def list(self, request, project_pk=None, *args, **kwargs):
        """
        overide list action to filter issues by project.
        """

        project = get_object_or_404(Project, pk=project_pk)
        queryset = Issue.objects.filter(project=project_pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset, many=True)
        return Response(serializer.data)

    def update(self, request, project_pk=None, *args, **kwargs):
        """
        overide update action to fill the author_user and project fields.
        """

        project = get_object_or_404(Project, pk=project_pk)
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        request_data["project"] = project_pk
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class CommentViewset(ModelViewSet):
    """
    This view allows all CRUD actions but only
    with some permissions.
    Some actions are overide to fill automaticaly some fields.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get a query set of all comment of a specific issue.
        """

        issue = get_object_or_404(Issue, pk=self.kwargs["issue_id"])
        return Comment.objects.filter(issue_id=issue)

    def create(self, request, issue_pk=None, *args, **kwargs):
        """
        overide create action to fill the author_user and issue_id fields.
        """
        issue = get_object_or_404(Issue, pk=self.kwargs["issue_id"])
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        request_data["issue_id"] = issue.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, issue_pk=None, *args, **kwargs):
        """
        overide update action to fill the author_user and issue_id fields.
        """

        issue = get_object_or_404(Issue, pk=self.kwargs["issue_id"])
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        request_data["issue_id"] = issue.id
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ContributorsViewset(ModelViewSet):
    """
    This view allows all CRUD actions but only
    with some permissions.
    Some actions are overide to fill automaticaly some fields.
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get a query set of all contributors.
        """
        return Contributor.objects.all()

    def list(self, request, project_pk=None):
        """
        overide list action to filter comment by project.
        """
        project = get_object_or_404(Project, pk=project_pk)
        self.check_object_permissions(request, project)
        queryset = Contributor.objects.filter(projects=project_pk)
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, project_pk=None):
        """
        overide create action to check permission.
        """
        project = get_object_or_404(Project, pk=project_pk)
        self.check_object_permissions(request, project)
        request_data = request.data.copy()
        request_data.update(
            {
                "projects": project_pk,
                "permission": "Contributeur",
            }
        )
        serializer = ContributorSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
