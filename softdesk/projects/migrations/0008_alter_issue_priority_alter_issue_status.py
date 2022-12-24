# Generated by Django 4.1.4 on 2022-12-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_comment_author_user_alter_issue_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="priority",
            field=models.CharField(
                choices=[
                    ("High priority", "Priorite Haute"),
                    ("Medium priority", "Priorite Moyenne"),
                    ("Low priority", "Priorite Basse"),
                ],
                default="Low priority",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="issue",
            name="status",
            field=models.CharField(
                choices=[
                    ("To do", "A Faire"),
                    ("Wip", "En Cours"),
                    ("COMPLETE", "Terminer"),
                ],
                default="To do",
                max_length=128,
            ),
        ),
    ]