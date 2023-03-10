"""
The serializer for project, issue, contributor & comment.
"""
from rest_framework import serializers

from projects.models import Project, Issue, Comment, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    """
    The contributor serializer.
    """

    class Meta:
        """
        The model's contributor.
        """

        model = Contributor
        fields = [
            "id",
            "user_id",
            "permission",
            "role",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """
    The project serializer.
    """

    contributors = serializers.SerializerMethodField()

    def get_contributors(self, instance):

        return Contributor.objects.filter(project=instance).values("user_id__username")

    class Meta:
        """
        The model's project.
        """

        model = Project
        fields = ["id", "title", "description", "type", "author_user", "contributors"]

    def validate_project(self, value):
        """
        Check if a project already exist.
        """
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError("Le projet existe déjà")
        return value


class IssuesSerializer(serializers.ModelSerializer):
    """
    The issue serializer.
    """

    class Meta:
        """
        The model's issue.
        """

        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "project",
            "tag",
            "priority",
            "status",
            "author_user",
            "assignee_user",
            "time_created",
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    The comment serializer.
    """

    class Meta:
        """
        The model's comment.
        """

        model = Comment
        fields = [
            "id",
            "description",
            "issue_id",
            "author_user",
            "time_created",
        ]
