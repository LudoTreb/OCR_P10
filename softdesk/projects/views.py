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
    For the create's action is override
    to add contributors fields
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        return Project.objects.all()

    def create(self, request):
        pass

    def destroy(self, request,):
        pass


class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()


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
