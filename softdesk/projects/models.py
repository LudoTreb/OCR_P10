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

        WEBSITE = "WS"
        IOS = "IOS"
        ANDROID = "ANDRIOD"

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    type = models.fields.CharField(
        choices=Type.choices, max_length=128, default="WEBSITE"
    )
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Issue(models.Model):
    """
    The Issue model.
    """

    class Tag(models.TextChoices):
        """
        The choice for tagging issue
        """

        AMELIORATION = "AM"
        FONCTIONNALITE = "FCN"
        BOGUE = "BG"

    class Priority(models.TextChoices):
        """
        The choice for priority
        """

        PRIORITE_HAUTE = "PH"
        PRIORITE_MOYENNE = "PM"
        PRIORITE_BASSE = "PB"

    class Status(models.TextChoices):
        """
        The choice for status
        """

        A_FAIRE = "AF"
        EN_COURS = "EC"
        TERMINER = "T"

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    tag = models.CharField(choices=Tag.choices, max_length=128)
    priority = models.CharField(choices=Priority.choices, max_length=128)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, max_length=128, default="A faire")
    # author_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name="author_user_id",
    # )
    # assignee_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name="assignee_user_id",
    # )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    The comment model.
    """

    description = models.TextField(max_length=8192, blank=True)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    # author_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_user_id"
    # )
    time_created = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    """
    The contributor model.
    """

    class Permission(models.TextChoices):
        """
        The choice for permission.
        """

        AUTEUR = "AUTHOR"
        CONTRIBUTEUR = "CONTRIBUTOR"

    class Role(models.TextChoices):
        """
        The choice for the role.
        """

        CLIENT = "CLIENT"
        DEV = "DEVELOPPEUR"

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    permission = models.CharField(choices=Permission.choices, max_length=128)
    role = models.CharField(choices=Role.choices, max_length=128)
