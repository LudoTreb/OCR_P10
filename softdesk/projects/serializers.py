from rest_framework import serializers
from projects.models import Project, Issue, Comment, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user"]

    def validate_project(self, value):
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError("Le projet existe déjà")
        return value


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "project",
            "tag",
            "priority",
            "status",
            'author_user',
            'assignee_user',
            "time_created",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "issue_id",
            'author_user',
            "time_created",
        ]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "id",
            "user_id",
            "projects",
            "permission",
            "role",
        ]
