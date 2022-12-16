from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from projects.models import Project, Issue, Comment, Contributor
from projects.serializers import (
    ProjectSerializer,
    IssuesSerializer,
    CommentSerializer,
    ContributorSerializer,
)


class AdminProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer


    def get_queryset(self):
        return Project.objects.all()

    def create(self, request):
        pass

    def destroy(self, request):
        pass


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()




class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
