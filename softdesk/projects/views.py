from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Issues, Comments, Contributors
from projects.serializers import (
    ProjectSerializer,
    IssuesSerializer,
    CommentSerializer,
    ContributorSerializer,
)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()




class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issues.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.all()


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributors.objects.all()
