"""
Models for project, issue, contributor, comment.
"""
from django.conf import settings
from django.db import models


class Project(models.Model):
    """
    The project model.
    """

    class Type(models.TextChoices):
        """
        The choice for type of project
        """

        FRONTEND = "Front-end"
        BACKTEND = "Back-end"
        IOS = "Ios"
        ANDROID = "Android"

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    type = models.fields.CharField(
        choices=Type.choices, max_length=128, default=Type.FRONTEND
    )
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"


class Issue(models.Model):
    """
    The Issue model.
    """

    class Tag(models.TextChoices):
        """
        The choice for tagging issue
        """

        AMELIORATION = "Improvement"
        FONCTIONALITE = "Feature"
        BOGUE = "Bug"

    class Priority(models.TextChoices):
        """
        The choice for priority
        """

        PRIORITE_HAUTE = "High priority"
        PRIORITE_MOYENNE = "Medium priority"
        PRIORITE_BASSE = "Low priority"

    class Status(models.TextChoices):
        """
        The choice for status
        """

        A_FAIRE = "To do"
        EN_COURS = "Wip"
        TERMINER = "COMPLETE"

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    priority = models.CharField(
        choices=Priority.choices, max_length=128, default=Priority.PRIORITE_BASSE
    )
    tag = models.CharField(choices=Tag.choices, max_length=128, default=Tag.BOGUE)
    status = models.CharField(
        choices=Status.choices, max_length=128, default=Status.A_FAIRE
    )
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_user",
        null=True,
    )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_user",
        null=True,
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """
    The comment model.
    """

    description = models.TextField(max_length=8192, blank=True)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comment_author_user",
    )
    time_created = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    """
    The contributor model.
    """

    class Permission(models.TextChoices):
        """
        The choice for permission.
        """

        AUTHOR = "Auteur"
        CONTRIBUTOR = "Contributeur"

    class Role(models.TextChoices):
        """
        The choice for the role.
        """

        CLIENT = "Client"
        DEV = "Développeur"

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    projects = models.ManyToManyField(
        to=Project,
    )
    permission = models.CharField(choices=Permission.choices, max_length=128)
    role = models.CharField(choices=Role.choices, max_length=128, default=Role.CLIENT)
