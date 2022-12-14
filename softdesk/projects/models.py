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
    # Vérifier ce que fait ce champ et modifier en focntion
    type = models.fields.CharField(
        choices=Type.choices, max_length=128, default="WEBSITE"
    )
    # définir dans les settings AUTH_USER_MODEL
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Issues(models.Model):
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
    # définir dans les settings AUTH_USER_MODEL
    # author_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_user_id"
    # )
    # assignee_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee_user_id"
    # )
    time_created = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """
    The comment model.
    """

    description = models.TextField(max_length=8192, blank=True)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    # définir dans les settings AUTH_USER_MODEL
    # author_user_id = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_user_id"
    # )
    time_created = models.DateTimeField(auto_now_add=True)


class Contributors(models.Model):
    """
    The contributor model.
    """

    class Permission(models.TextChoices):
        """
        The choice for permission.
        """

        ...

    class Role(models.TextChoices):
        """
        The choice for the role.
        """

        ...

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    permission = models.CharField(choices=Permission.choices, max_length=128)
    role = models.CharField(choices=Role.choices, max_length=128)
