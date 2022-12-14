from rest_framework import serializers
from projects.models import Project, Issues, Comments, Contributors


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user_id"]

    def validate_project(self, value):
        if Project.objects.filter(title=value).exists():
            raise serializers.ValidationError("Le projet existe déjà")
        return value


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            # 'author_user_id',
            # 'assignee_user_id',
            "time_created",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "id",
            "description",
            "issue_id",
            # 'author_user_id',
            "time_created",
        ]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = [
            "id",
            "user_id",
            "project_id",
            "permission",
            "role",
        ]
