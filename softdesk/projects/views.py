from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment, Contributor
from projects.permissions import IsProjectAuthor

from projects.serializers import (
    ProjectSerializer,
    IssuesSerializer,
    CommentSerializer,
    ContributorSerializer,
)


class ProjectViewset(ModelViewSet):
    """
    This view allows all CRUD actions.
    The create action is override
    to add contributors fields
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        return Project.objects.filter(author_user=self.request.user)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()

    def create(self, request, project_pk=None, *args, **kwargs):
        project = get_object_or_404(Project, pk=project_pk)
        request_data = request.data.copy()
        request_data["author_user"] = request.user.id
        request_data["project"] = project_pk
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, project_pk=None, *args, **kwargs):
        project = get_object_or_404(Project, pk=project_pk)
        queryset = Issue.objects.filter(project=project_pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset, many=True)
        return Response(serializer.data)


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.all()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.all()

    # def list(self, request, project_pk=None):
    #     """ GET all projects if permission"""
    #     project = get_object_or_404(Project, pk=project_pk)
    #     self.check_object_permissions(request, project)
    #     queryset = Contributor.objects.filter(project=project_pk)
    #     serializer = ContributorSerializer(queryset, many=True)
    #     return Response(serializer.data)
