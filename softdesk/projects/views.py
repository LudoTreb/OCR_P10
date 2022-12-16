from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issue, Comment, Contributor
from projects.serializers import (
    ProjectSerializer,
    IssuesSerializer,
    CommentSerializer,
    ContributorSerializer,
)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.all()

    def create(self, request):
        pass

    def destroy(self, request):
        pass


class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.all()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contributor.objects.all()
